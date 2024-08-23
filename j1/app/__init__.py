from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import auth, products, cart, payment, orders
    app.register_blueprint(auth.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(payment.bp)
    app.register_blueprint(orders.bp)

    return app
