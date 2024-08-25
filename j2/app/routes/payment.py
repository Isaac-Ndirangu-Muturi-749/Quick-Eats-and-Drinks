# app/routes/payment.py
from flask import Blueprint, url_for, redirect, request, flash
import paypalrestsdk
from app.models import Order, OrderItem, Product
from app import db
from flask_login import current_user

payment_bp = Blueprint('payment', __name__, url_prefix='/payment')

@payment_bp.route('/create_payment', methods=['POST'])
def create_payment():
    # Retrieve order details from the form or session
    order_id = request.form.get('order_id')
    order = Order.query.get(order_id)

    if not order or order.user_id != current_user.id:
        flash('Invalid order or unauthorized access', 'danger')
        return redirect(url_for('orders.order_history'))

    total_amount = order.total_amount

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": url_for('payment.execute_payment', _external=True),
            "cancel_url": url_for('payment.cancel_payment', _external=True)
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Order {}".format(order_id),
                    "sku": "order_{}".format(order_id),
                    "price": "{:.2f}".format(total_amount),
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {"total": "{:.2f}".format(total_amount), "currency": "USD"},
            "description": "Payment for Order {}".format(order_id)
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        flash('Payment creation failed', 'danger')
        return redirect(url_for('orders.order_history'))


@payment_bp.route('/execute_payment', methods=['GET'])
def execute_payment():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')
    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        # Update order status
        order_id = payment.transactions[0].item_list.items[0].sku.split('_')[1]
        order = Order.query.get(order_id)
        if order:
            order.status = 'Completed'
            db.session.commit()
        return redirect(url_for('orders.order_history', order_id=order_id))
    else:
        flash('Payment execution failed', 'danger')
        return redirect(url_for('orders.order_history'))


@payment_bp.route('/cancel_payment', methods=['GET'])
def cancel_payment():
    flash('Payment was canceled', 'warning')
    return redirect(url_for('orders.order_history'))
