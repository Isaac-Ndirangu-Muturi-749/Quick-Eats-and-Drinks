# app/routes/products.py

from flask import Blueprint, request, render_template, redirect, url_for
from app import db
from app.models import Product

bp = Blueprint('products', __name__)

@bp.route('/menu', methods=['GET'])
def menu():
    products_list = Product.query.all()
    return render_template('menu.html', products=products_list)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/order-history')
def order_history():
    # Logic to retrieve and display order history
    return render_template('order_history.html')

@bp.route('/process_order', methods=['POST'])
def process_order():
    # Handle order processing
    return redirect(url_for('products.menu'))
