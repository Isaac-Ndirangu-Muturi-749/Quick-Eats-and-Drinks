from functools import wraps
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Product, User, ProductGroup
from flask_login import login_required, current_user

# Define your admin blueprint
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Admin check decorator
def admin_required(func):
    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            flash("You are not authorized to access this page.", "danger")
            return redirect(url_for('main.index'))
        return func(*args, **kwargs)
    return wrapper

# Product management routes
@admin_bp.route('/products', methods=['GET'])
@admin_required
def product_list():
    products = Product.query.all()
    return render_template('admin/product_list.html', products=products)

@admin_bp.route('/products/add', methods=['GET', 'POST'])
@admin_required
def add_product():
    product_groups = ProductGroup.query.all()  # Query all product groups
    if request.method == 'POST':
        product_name = request.form['product_name']
        description = request.form.get('description')
        price = float(request.form['price'])
        product_group_id = int(request.form['product_group_id'])  # Group selection
        image_url = request.form.get('image_url')

        # Create and add new product
        new_product = Product(
            product_name=product_name,
            description=description,
            price=price,
            product_group_id=product_group_id,  # Associate with selected group
            image_url=image_url
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin.product_list'))

    return render_template('admin/add_product.html', product_groups=product_groups)

@admin_bp.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
@admin_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    product_groups = ProductGroup.query.all()  # Query all product groups

    if request.method == 'POST':
        product.product_name = request.form['product_name']
        product.description = request.form.get('description')
        product.price = float(request.form['price'])
        product.product_group_id = int(request.form['product_group_id'])  # Update group
        product.image_url = request.form.get('image_url')

        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin.product_list'))

    return render_template('admin/edit_product.html', product=product, product_groups=product_groups)

@admin_bp.route('/products/delete/<int:product_id>', methods=['POST'])
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin.product_list'))

# Product group management routes
@admin_bp.route('/product_groups', methods=['GET'])
@admin_required
def product_group_list():
    product_groups = ProductGroup.query.all()
    return render_template('admin/product_group_list.html', product_groups=product_groups)

@admin_bp.route('/product_groups/add', methods=['GET', 'POST'])
@admin_required
def add_product_group():
    if request.method == 'POST':
        group_name = request.form['product_group_name']

        # Create and add new product group
        new_group = ProductGroup(product_group_name=group_name)
        db.session.add(new_group)
        db.session.commit()
        flash('Product group added successfully!', 'success')
        return redirect(url_for('admin.product_group_list'))

    return render_template('admin/add_product_group.html')

@admin_bp.route('/product_groups/edit/<int:group_id>', methods=['GET', 'POST'])
@admin_required
def edit_product_group(group_id):
    group = ProductGroup.query.get_or_404(group_id)

    if request.method == 'POST':
        group.product_group_name = request.form['product_group_name']

        db.session.commit()
        flash('Product group updated successfully!', 'success')
        return redirect(url_for('admin.product_group_list'))

    return render_template('admin/edit_product_group.html', group=group)

@admin_bp.route('/product_groups/delete/<int:group_id>', methods=['POST'])
@admin_required
def delete_product_group(group_id):
    group = ProductGroup.query.get_or_404(group_id)
    db.session.delete(group)
    db.session.commit()
    flash('Product group deleted successfully!', 'success')
    return redirect(url_for('admin.product_group_list'))

# User management routes
@admin_bp.route('/users', methods=['GET'])
@admin_required
def user_list():
    users = User.query.all()
    return render_template('admin/user_list.html', users=users)

@admin_bp.route('/users/promote/<int:user_id>', methods=['POST'])
@admin_required
def promote_user(user_id):
    user = User.query.get_or_404(user_id)
    if not user.is_admin:
        user.is_admin = True
        db.session.commit()
        flash('User promoted to admin successfully!', 'success')
    else:
        flash('User is already an admin.', 'info')
    return redirect(url_for('admin.user_list'))

@admin_bp.route('/users/demote/<int:user_id>', methods=['POST'])
@admin_required
def demote_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_admin:
        user.is_admin = False
        db.session.commit()
        flash('User demoted successfully!', 'success')
    else:
        flash('User is not an admin.', 'info')
    return redirect(url_for('admin.user_list'))

# Dashboard route
@admin_bp.route('/dashboard', methods=['GET'])
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')
