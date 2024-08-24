from flask import Blueprint, render_template
from app.models import Product, ProductGroup
from datetime import datetime

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/menu', methods=['GET'])
def menu():
    # Fetch all product groups and their associated products in a single query
    product_groups = ProductGroup.query.outerjoin(Product).all()

    # Create a dictionary to store products by group
    grouped_products = {}

    # Initialize the total product count
    total_products_count = 0

    # Loop through each group and fetch products
    for group in product_groups:
        products = group.products  # Assuming you have a relationship set up between ProductGroup and Product
        grouped_products[group.product_group_name] = products
        total_products_count += len(products)

    return render_template('products/menu.html', grouped_products=grouped_products, total_products_count=total_products_count)
