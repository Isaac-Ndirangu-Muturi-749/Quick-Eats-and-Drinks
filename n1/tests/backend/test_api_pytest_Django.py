from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app.models import Product, User

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', email='testuser@example.com', password='password')
        self.product = Product.objects.create(name='Frozen Pizza', price=10.00, description='Delicious frozen pizza')

    def test_get_products(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Frozen Pizza', str(response.content))
