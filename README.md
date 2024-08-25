
# Quick Eats & Drinks

**Quick Eats & Drinks** is a web-based e-commerce platform designed for managing and ordering food and drinks. This application allows users to browse products, place orders, and manage their order history. The platform also includes an admin interface for managing products, product groups, and users.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Quick Eats & Drinks provides a user-friendly interface for managing food and drink orders. Users can view products by category, place orders, and track their order history. Administrators have access to a dashboard where they can add, edit, or delete products and product groups.

## Features

- **User Authentication**: Sign up, log in, and manage user accounts.
- **Product Management**: Browse products, view details, and add items to the cart.
- **Order Processing**: Place orders and proceed to checkout.
- **Order History**: View past orders and track order status.
- **Admin Interface**: Manage products, product groups, and user accounts.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technology Stack

- **Frontend**: HTML, CSS (stylesheets in `static/css`), JavaScript (in `static/js/menu.js`).
- **Backend**: Flask (Python framework), SQLAlchemy (ORM for database management).
- **Database**: SQLite (for development and testing), PostgreSQL (for production).
- **Payment Integration**: PayPal.
- **Testing**: pytest for integration testing.

## Setup and Installation

To set up and run the Quick Eats & Drinks project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Isaac-Ndirangu-Muturi-749/Quick-Eats-and-Drinks.git
   cd Quick-Eats-and-Drinks
   ```

2. **Create a Virtual Environment**:

   ```bash
    conda create --name my_env python=3.10
    conda activate my_env
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Setup Environment Configuration

This section provides instructions for creating and configuring the `.env` file and integrating PayPal API credentials into the application.

1. **Create a `.env` File**

   Create a file named `.env` in the root directory of the project. This file should contain environment-specific variables, such as database configurations and secret keys. Below is a template you can use:

   ```ini
   # .env

   # Database Configuration
   DATABASE_URL=sqlite:///instance/site.db

   # PayPal Configuration
   PAYPAL_CLIENT_ID=your_paypal_client_id
   PAYPAL_CLIENT_SECRET=your_paypal_client_secret

   # Secret Key for Flask Sessions
   SECRET_KEY=your_secret_key
   ```

   Replace `your_paypal_client_id`, `your_paypal_client_secret`, and `your_secret_key` with your actual PayPal API credentials and Flask secret key.

  The application is properly configured to load the `.env` variables. You can use the `python-dotenv` package to load environment variables from the `.env` file. Install it using:

   ```bash
   pip install python-dotenv
   ```

2. **Setup PayPal API**

   Make sure to have your PayPal API credentials ready. You need to configure the PayPal SDK with your credentials to handle payment processing. You can add these credentials to your `.env` file as shown above. The PayPal API client will use these credentials to communicate with the PayPal services.

   Then, in the application setup (i.e., `app/__init__.py`), the environment variables are loaded like this:

   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()

   # Example of accessing environment variables
   PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
   PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET')
   SECRET_KEY = os.getenv('SECRET_KEY')
   ```

   The PayPal payment routes and configurations are correctly set up to use these environment variables.


4. **Setup the Database**:

## Setup the Database

Follow these steps to set up and initialize the database:

a. **Remove Existing Migrations Folder and Database File**:

   ```bash
   sudo rm -rf ./migrations/
   sudo rm -f ./instance/site.db
   ```

b. **Initialize the Migration Repository**:

   ```bash
   flask db init
   ```

c. **Generate an Initial Migration Script**:

   ```bash
   flask db migrate -m "Initial migration."
   ```

d. **Apply the Migration to the Database**:

   ```bash
   flask db upgrade
   ```

e. **Create the Admin User**:

   ```bash
   python create_admin.py
   ```

f. **Seed the Database with Initial Data**:

   ```bash
   python seed.py
   ```

   Alternatively, you can use the following command to initialize and seed the database:

   ```bash
   python db_setup_and_seed.py
   ```

5. **Run the Application**:

   ```bash
   python run.py
   ```

   The application will be available at `http://127.0.0.1:5000`.

## Running Tests

To run the tests for the project, use:

   ```bash
   python run_tests.py
   ```
   Alternatively, you can use the following command:

    ```bash
    pytest
    ```

This will run all the tests defined in the `tests` directory and ensure that everything is functioning as expected.

## Folder Structure

- **app/**: Contains the core application code including routes, models, and static assets.
  - **routes/**: Contains route handlers for different functionalities.
  - **static/**: Contains CSS, JavaScript, and image files.
  - **templates/**: Contains HTML templates for rendering views.
- **create_admin.py**: Script to create an admin user.
- **db_setup_and_seed.py**: Script to set up and seed the database.
- **instance/**: Directory for instance-specific configuration and database files.
- **migrations/**: Contains database migration files.
- **requirements.txt**: Lists the project dependencies.
- **run.py**: Entry point to run the application.
- **run_tests.py**: Script to run tests.
- **seed.py**: Script for seeding the database with initial data.
- **tests/**: Contains test files for the application.

## Contributing

Contributions are welcome! Please follow these guidelines for contributing:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Follow me on Twitter 🐦, connect with me on LinkedIn 🔗, and check out my GitHub 🐙. You won't be disappointed!

🐦 Twitter: https://x.com/NdiranguMuturi1
💼 LinkedIn: https://www.linkedin.com/in/isaac-muturi-3b6b2b237
🔗 GitHub: https://github.com/Isaac-Ndirangu-Muturi-749
📧 Email: ndirangumuturi749@gmail.com
