from flask import Blueprint, render_template, redirect, url_for, request, flash

bp = Blueprint('payment', __name__, url_prefix='/payment')

@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Payment processing logic (e.g., using PayPal API)
        flash('Payment successful')
        return redirect(url_for('orders.view_orders'))
    return render_template('checkout.html')
