# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object('app.config.Config')
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)

    # Custom template filter
    @app.template_filter('format_currency')
    def format_currency(value):
        """Formats a number as currency"""
        return "${:,.2f}".format(value)

    # Import and register blueprints
    from app.routes.products import bp as products_bp
    app.register_blueprint(products_bp)

    return app
