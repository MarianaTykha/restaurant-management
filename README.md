# Restaurant Management System

Restaurant Management is a Django-based web application designed to streamline
restaurant operations, including dish management, chef assignments,  and menu organization.
The project is structured to be easily extendable and customizable.

## Features

- Manage dishes and their categories
- Assign chefs to dishes
- Handle orders from customers
- Responsive UI with Django Material Kit
- View order status and kitchen progress
- Environment variable management for security (e.g. SECRET_KEY)
- Many-to-Many relationships for ingredients (optional feature)

## Technologies Used
- Python
- Django
- PostgreSQL (or SQLite for development)
- Bootstrap (via Django Material Kit)
- Docker (optional for deployment)

## Installation

1. Prerequisites (Ensure you have the following installed:)
- Python 3.x
- pip
- virtualenv (optional but recommended)

## Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/MarianaTykha/restaurant-management.git cd restaurant-management
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
    ```bash
   pip install -r requirements.txt
   
4. Apply migrations:
    ```bash
   python manage.py migrate

5. Create a superuser:
    ```bash
   python manage.py createsuperuser

6. Run the server:
    ```bash
   python manage.py runserver
   
7. Open the project in your browser:
    ```bash
   http://127.0.0.1:8000/
   
# Usage

- Navigate to the admin panel (/admin/) to manage dishes, chefs, and menu items
- Assign chefs to dishes and update menu items dynamically
- Use user authentication to access restricted features

# Contribution

Contributions are welcome! If you'd like to contribute:
- Fork the repository
- Create a new branch (git checkout -b feature-branch)
- Commit your changes (git commit -m "Add new feature")
- Push to the branch (git push origin feature-branch)
- Open a Pull Request

# License

This project is licensed under the MIT License.

# Contact
For questions or suggestions, feel free to reach out via GitHub Issues.