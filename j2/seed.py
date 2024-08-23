from app import create_app, db
from app.models import User, Product, Order, OrderItem
from faker import Faker

app = create_app()
fake = Faker()

def seed_data():
    with app.app_context():
        # Add sample users
        users = [
            User(username='johndoe', email='johndoe@example.com', password_hash='hashedpassword1'),
            User(username='janedoe', email='janedoe@example.com', password_hash='hashedpassword2'),
        ]
        db.session.bulk_save_objects(users)
        db.session.commit()

        # Add sample products
        products = [
            Product(product_name='Burger', description='Delicious beef burger', price=5.99, product_group_number=1, product_group_name='Burgers', image_url='http://example.com/burger.jpg'),
            Product(product_name='Pizza', description='Cheese pizza', price=8.99, product_group_number=2, product_group_name='Pizzas', image_url='http://example.com/pizza.jpg'),
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

        # Add sample orders and order items
        user = User.query.first()  # Get the first user
        order = Order(user_id=user.id, amount=14.98)
        db.session.add(order)
        db.session.commit()

        burger = Product.query.filter_by(product_name='Burger').first()
        pizza = Product.query.filter_by(product_name='Pizza').first()

        order_item_burger = OrderItem(order_id=order.id, product_id=burger.id, quantity=1, amount=burger.price)
        order_item_pizza = OrderItem(order_id=order.id, product_id=pizza.id, quantity=1, amount=pizza.price)

        db.session.add_all([order_item_burger, order_item_pizza])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
