import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from app.models import Product, Order, User

def seed_data():
    # Create sample products
    products = [
        {'name': 'Frozen Pizza', 'price': 10.00, 'description': 'Delicious frozen pizza'},
        {'name': 'Pre-cooked Chicken Breasts', 'price': 12.00, 'description': 'Tender and juicy chicken breasts'},
        {'name': 'Instant Noodles', 'price': 5.00, 'description': 'Quick and easy instant noodles'},
        {'name': 'Potato Chips', 'price': 3.00, 'description': 'Crispy potato chips'},
        {'name': 'Granola Bars', 'price': 4.00, 'description': 'Healthy granola bars'},
        {'name': 'Mixed Nuts', 'price': 6.00, 'description': 'Assorted mixed nuts'},
    ]

    for product_data in products:
        Product.objects.create(**product_data)

    # Create sample users
    users = [
        {'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'password': 'password456'},
    ]

    for user_data in users:
        User.objects.create(**user_data)

    # Create sample orders
    orders = [
        {'user': User.objects.get(username='john_doe'), 'product': Product.objects.get(name='Frozen Pizza'), 'quantity': 2},
        {'user': User.objects.get(username='jane_smith'), 'product': Product.objects.get(name='Instant Noodles'), 'quantity': 5},
    ]

    for order_data in orders:
        Order.objects.create(**order_data)

if __name__ == "__main__":
    seed_data()
