# Restaurant Management System

This project is a restaurant management system designed to manage dishes, chefs, orders, and more. It allows for easy management of kitchen services, orders, and customers. The system is built using Django and follows a class-based view approach for all views.

## Features

- Manage dishes and their categories
- Assign chefs to dishes
- Handle orders from customers
- View order status and kitchen progress
- Environment variable management for security (e.g. SECRET_KEY)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/restaurant-management.git
   
2. Install dependencies:
 pip install -r requirements.txt

3. Create and apply migrations:
 python manage.py migrate

4. Run the server:
 python manage.py runserver

# Environment Variables

SECRET_KEY: A secret key for Django settings (make sure it's kept secure).

Other environment variables as needed.