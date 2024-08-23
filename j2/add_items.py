# add_items.py

from app import create_app, db
from app.models import Product

def add_items():
    products = [
        Product(product_name='Pizza', price=12.99, description='Delicious cheese pizza', image_url='https://th.bing.com/th/id/OIP.8UeIFPMYwIErE1ShRYB9QAHaEo?rs=1&pid=ImgDetMain', product_group_number=1, product_group_name='Main Course'),
        Product(product_name='Burger', price=8.99, description='Juicy beef burger', image_url='burger.jpg', product_group_number=1, product_group_name='Main Course'),
        Product(product_name='Pasta', price=10.99, description='Creamy Alfredo pasta', image_url='pasta.jpg', product_group_number=1, product_group_name='Main Course'),
        Product(product_name='Salad', price=7.99, description='Fresh garden salad', image_url='salad.jpg', product_group_number=1, product_group_name='Appetizers'),
        Product(product_name='Ice Cream', price=5.99, description='Vanilla ice cream with chocolate sauce', image_url='https://th.bing.com/th/id/OIP._xwTuw8WFnoy7ZmFi1zBMQHaNK?w=115&h=180&c=7&r=0&o=5&pid=1.7', product_group_number=2, product_group_name='Desserts'),
        Product(product_name='Soda', price=1.99, description='Refreshing cola drink', image_url='soda.jpg', product_group_number=2, product_group_name='Beverages'),
        Product(product_name='Cake', price=6.99, description='Chocolate cake with frosting', image_url='https://th.bing.com/th/id/OIP.Fw-199hoU0qcuFHEL9Vf8wHaLH?w=195&h=293&c=7&r=0&o=5&pid=1.7', product_group_number=2, product_group_name='Desserts'),
        Product(product_name='Smoothie', price=4.99, description='Fruit smoothie with banana and berries', image_url='smoothie.jpg', product_group_number=2, product_group_name='Beverages'),
    ]
    db.session.bulk_save_objects(products)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        add_items()
