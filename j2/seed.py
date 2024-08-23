from app import create_app, db
from app.models import Product

def seed_products():
    products = [
        Product(product_name='Pizza', description='Delicious cheese pizza', price=10.99, product_group_number=1, product_group_name='Pizza', image_url='pizza.png'),
        # Add more products as needed
    ]
    db.session.bulk_save_objects(products)
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_products()
