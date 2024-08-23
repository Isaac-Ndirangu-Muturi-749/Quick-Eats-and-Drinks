from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    product_group_number = db.Column(db.Integer, nullable=False)
    product_group_name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
