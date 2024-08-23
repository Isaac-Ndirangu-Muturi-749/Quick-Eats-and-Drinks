from flask import Blueprint, render_template, redirect, url_for, request, flash

bp = Blueprint('cart', __name__, url_prefix='/cart')

cart_items = []  # Simulated cart storage (to be replaced by a database)

@bp.route('/', methods=['GET'])
def view_cart():
    return render_template('cart.html', items=cart_items)

@bp.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Logic to add product to cart
    # Placeholder: Append the product_id to cart_items
    cart_items.append(product_id)
    flash('Item added to cart!')
    return redirect(url_for('products.product_listing'))

@bp.route('/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    # Logic to remove product from cart
    cart_items.remove(product_id)
    flash('Item removed from cart!')
    return redirect(url_for('cart.view_cart'))
