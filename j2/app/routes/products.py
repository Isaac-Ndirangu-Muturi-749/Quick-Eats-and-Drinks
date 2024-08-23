from flask import Blueprint, request, render_template, redirect, url_for
from app import db
from app.models import Product, Order, OrderItem
from flask_login import current_user, login_required
from datetime import datetime

bp = Blueprint('products', __name__)

@bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/menu', methods=['GET'])
def menu():
    products_list = Product.query.all()
    return render_template('menu.html', products=products_list)

@bp.route('/order-history')
@login_required
def order_history():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    order_data = []

    for order in orders:
        items = OrderItem.query.filter_by(order_id=order.id).all()
        order_data.append({
            'order': order,
            'items': items
        })

    return render_template('order_history.html', orders=order_data)

@bp.route('/process_order', methods=['POST'])
@login_required
def process_order():
    product_ids = request.form.getlist('productId[]')
    quantities = request.form.getlist('quantity[]')
    prices = request.form.getlist('price[]')

    # Calculate total amount
    total_amount = sum(float(price) * int(quantity) for price, quantity in zip(prices, quantities))

    # Insert the order into the database
    order = Order(user_id=current_user.id, order_date_time=datetime.utcnow(), amount=total_amount)
    db.session.add(order)
    db.session.commit()

    # Insert order items
    for product_id, quantity, price in zip(product_ids, quantities, prices):
        if int(quantity) > 0:
            order_item = OrderItem(order_id=order.id, product_id=int(product_id), quantity=int(quantity), amount=float(price) * int(quantity))
            db.session.add(order_item)

    db.session.commit()

    return redirect(url_for('products.order_confirmation', order_id=order.id))

@bp.route('/order_confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    items = OrderItem.query.filter_by(order_id=order.id).all()

    return render_template('order_confirmation.html', order=order, items=items)
