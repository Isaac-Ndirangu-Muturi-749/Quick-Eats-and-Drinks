import unittest
from app import create_app, db
from app.models import Product, User

class ProductAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user = User(username='testuser', email='testuser@example.com', password='password')
        db.session.add(self.user)
        self.product = Product(name='Frozen Pizza', price=10.00, description='Delicious frozen pizza')
        db.session.add(self.product)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_products(self):
        response = self.client.get('/api/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Frozen Pizza', response.get_data(as_text=True))
