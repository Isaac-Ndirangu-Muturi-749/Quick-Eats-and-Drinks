from flask import Blueprint, render_template, request

bp = Blueprint('orders', __name__, url_prefix='/orders')

orders = []  # Simulated order storage (to be replaced by a database)

@bp.route('/', methods=['GET'])
def view_orders():
    # Logic to view order history
    return render_template('order_history.html', orders=orders)

@bp.route('/track/<int:order_id>', methods=['GET'])
def track_order(order_id):
    # Logic to track a specific order
    order = next((o for o in orders if o['id'] == order_id), None)
    if order:
        return render_template('order_tracking.html', order=order)
    return "Order not found", 404
