# app/routes/products.py
from flask import Blueprint, render_template
from ..models.Product import Product  # Import the Product model

bp = Blueprint('products', __name__, url_prefix='/products')

# Static product list for now, can be extended to dynamic fetching from a database
products = [
    {'id': 1, 'name': 'Frozen Pizza', 'price': 10, 'image_filename': 'frozen_pizza.jpg'},
    {'id': 2, 'name': 'Cola', 'price': 2, 'image_filename': 'cola.jpg'},
    # More static products can be added here
]

@bp.route('/', methods=['GET'])
def product_listing():
    # Render product listing with static data
    return render_template('product_listing.html', products=products)

@bp.route('/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

@bp.route('/menu', methods=['GET'])
def menu():
    # Assuming products are dynamically fetched from the database
    products = Product.query.all()
    return render_template('menu.html', products=products)
