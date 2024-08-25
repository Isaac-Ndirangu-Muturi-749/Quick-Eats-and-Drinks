import pytest
from app import create_app, db
from app.models import User, Product, ProductGroup, Order
from flask import url_for


@pytest.fixture
def app():
    # Create a test application instance
    app = create_app('testing')

    # Establish a context for the app
    with app.app_context():
        # Create the database and the database table
        db.create_all()

        # Insert test data into the database here if needed

        yield app

        # Drop the database after the test
        db.drop_all()

@pytest.fixture
def client(app):
    # Provide a test client
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_menu_page(client):
    # Test menu page load
    response = client.get('/products/menu')

    print(response.data)
    assert response.status_code == 200
    assert b"Products Menu" in response.data  # checking content in the page

def test_create_order(client, app):
    # Log in as a user
    with app.app_context():
        user = User(username='testuser', email='test@example.com', is_admin=True)
        user.set_password('password')
        db.session.add(user)
        db.session.commit()

        with client.session_transaction() as session:
            session['user_id'] = user.id
            print(f"Session User ID: {session.get('user_id')}")

        product_group = ProductGroup(
            product_group_name="Ready-Made Meals",
            description="Convenient meals that are easy to prepare or eat on the go."
        )

        db.session.add(product_group)
        db.session.commit()

        product = Product(
            product_name="Instant Noodles",
            price=5,
            image_url="https://th.bing.com/th/id/OIP.vdi_w2DUVDsv1EY1vHfDgAHaIc?rs=1&pid=ImgDetMain",
            description="Quick and tasty noodles, ready in minutes for a satisfying meal.",
            product_group_id=product_group.id  # Use the correct product group ID
        )

        db.session.add(product)
        db.session.commit()

        # Ensure that the user is logged in
        with client.session_transaction() as session:
            assert session.get('user_id') == user.id

        client.post(url_for('auth.login'), data={
                'email': 'test@example.com',
                'password': 'password'

        })

        # Simulate creating an order
        response = client.post('/orders/process_order', data={
            'productId[]': [product.id],
            'productName[]': [product.product_name],
            'price[]': [product.price],
            'quantity[]': [1]
        })

        # Debugging response location
        print(f"Response Location: {response.location}")

        # Ensure redirection to the checkout page
        assert response.status_code == 302
        assert '/orders/checkout/' in response.location


def test_order_history(client, app):
    # Log in as a user
    with app.app_context():
        user = User.query.first()
        if user is None:
            user = User(username='testuser', email='test@example.com', is_admin=True)
            user.set_password('password')
            db.session.add(user)
            db.session.commit()
        with client.session_transaction() as session:
            session['user_id'] = user.id


        client.post(url_for('auth.login'), data={
                'email': 'test@example.com',
                'password': 'password'

        })

        # Test order history page load
        response = client.get('/orders/order-history')
        assert response.status_code == 200
        assert b"Your Order History" in response.data  # Check content


def test_payment_flow(client, app):
    import os
    import paypalrestsdk
    # PayPal SDK configuration
    paypalrestsdk.configure({
        "mode": "sandbox",  # Use sandbox mode for testing
        "client_id": os.getenv("PAYPAL_CLIENT_ID"),
        "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
    })

    with app.app_context():
        # Add a user if none exists
        user = User.query.first()
        if user is None:
            user = User(username='testuser', email='test@example.com', is_admin=True)
            user.set_password('password')
            db.session.add(user)
            db.session.commit()

        # Add an order
        order = Order(user_id=user.id, total_amount=20.00)
        db.session.add(order)
        db.session.commit()

        with client.session_transaction() as session:
            session['user_id'] = user.id

        # Log in the user
        client.post(url_for('auth.login'), data={
            'email': 'test@example.com',
            'password': 'password'
        })

        # Simulate payment creation
        response = client.post('/payment/create_payment', data={
            'order_id': order.id,
        })

        # Ensure redirection to the PayPal approval URL
        assert response.status_code == 302
        assert 'www.sandbox.paypal.com' in response.location
        assert 'express-checkout' in response.headers['Location']
