from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object('app.config.Config')
    app.config['TEMPLATES_AUTO_RELOAD'] = True

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

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Local import to avoid circular import issues
        return User.query.get(int(user_id))

    return app
