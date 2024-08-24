from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

# Initialize the app
app = create_app()

with app.app_context():
    # Create admin user
    admin_user = User(
        username='admin',
        email='admin@example.com',
        password_hash=generate_password_hash('admin', method='pbkdf2:sha256'),  # Use a supported method
        is_admin=True
    )

    # Add and commit the new user
    db.session.add(admin_user)
    db.session.commit()

    print('Admin user created successfully!')
