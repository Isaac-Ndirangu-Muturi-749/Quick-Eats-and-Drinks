from flask import Blueprint, render_template

bp = Blueprint('products', __name__, url_prefix='/products')

products = [
    {'id': 1, 'name': 'Frozen Pizza', 'price': 10, 'image_filename': 'frozen_pizza.jpg'},
    {'id': 2, 'name': 'Cola', 'price': 2, 'image_filename': 'cola.jpg'},
    # Add more products with 'image_filename' as needed
]


@bp.route('/', methods=['GET'])
def product_listing():
    return render_template('product_listing.html', products=products)

@bp.route('/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

# Add this route for the homepage
@bp.route('/')
def index():
    return render_template('index.html')
