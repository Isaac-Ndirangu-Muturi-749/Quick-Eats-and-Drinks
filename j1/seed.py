from app import create_app, db
from app.models.Product import Product

def seed_products():
    products = [
        Product(name="Frozen Pizza", price=10.00, image_filename="frozen_pizza.jpg"),
        Product(name="Cola", price=2.00, image_filename="cola.jpg"),
        # Add more products as needed
    ]

    db.session.bulk_save_objects(products)
    db.session.commit()
    print("Database seeded with products!")

if __name__ == "__main__":
    # Create the app and push an application context
    app = create_app()  # Ensure create_app() is a function that creates the Flask app instance
    with app.app_context():
        seed_products()
