# app/__init__.py
import os
from flask import Flask
from dotenv import load_dotenv
import paypalrestsdk
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
babel = Babel()
login_manager = LoginManager()

# Load environment variables from .env
load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object('app.config.Config')
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # PayPal SDK configuration
    paypalrestsdk.configure({
        "mode": "sandbox",  # or "live" for production
        "client_id": os.getenv("PAYPAL_CLIENT_ID"),
        "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
    })

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Custom template filter
    @app.template_filter('format_currency')
    def format_currency(value):
        """Formats a number as currency"""
        return "${:,.2f}".format(value)

    # Import and register blueprints
    from app.routes.main import main_bp as main_bp
    app.register_blueprint(main_bp)

    from app.routes.auth import auth_bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.products import products_bp as products_bp
    app.register_blueprint(products_bp)

    from app.routes.orders import orders_bp as orders_bp
    app.register_blueprint(orders_bp)

    from app.routes.admin import admin_bp as admin_bp
    app.register_blueprint(admin_bp)

    from app.routes.payment import payment_bp as payment_bp
    app.register_blueprint(payment_bp)

    # User loader for login manager
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Local import to avoid circular import issues
        return User.query.get(int(user_id))

    return app
