import random
import re
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.security import generate_password_hash

# Determine the absolute paths to the static and templates folders
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(project_root, 'static')
template_dir = os.path.join(project_root, 'templates')

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('front_page.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register_role.html')

@app.route('/register/chef', methods=['GET'])
def show_chef_registration_form():
    return render_template('reg_chef.html')

@app.route('/register/chef', methods=['POST'])
def register_chef():
    # Extract all fields from the form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    birthday = request.form['birthday']
    employee_id = request.form['employee_id']

    # Validate the employee ID
    if validate_employee_id(employee_id, 'chef'):
        # Hash the password
        password_hash = generate_password_hash(password)
        # Here, add your database logic to save these details
        # Assume function save_to_database() which you would need to define according to your DB setup
        # save_to_database(first_name, last_name, email, password_hash, birthday, employee_id)

        return redirect(url_for('success_page'))
    else:
        return "Invalid ID", 400
    
    # New routes for delivery registration
@app.route('/register/delivery', methods=['GET'])
def show_delivery_registration_form():
    return render_template('reg_delivery.html')

@app.route('/register/delivery', methods=['POST'])
def register_delivery():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    birthday = request.form['birthday']
    employee_id = request.form['employee_id']

    if validate_employee_id(employee_id, 'delivery'):
        password_hash = generate_password_hash(password)
        # Implement the logic to save these details to your database
        return redirect(url_for('success_page'))
    else:
        return "Invalid ID", 400
    
@app.route('/register/importer', methods=['GET'])
def show_importer_registration_form():
    return render_template('reg_food_importer.html')

@app.route('/register/importer', methods=['POST'])
def register_importer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    birthday = request.form['birthday']
    employee_id = request.form['employee_id']

    if validate_employee_id(employee_id, 'food_importer'):
        password_hash = generate_password_hash(password)
        # Add logic for database interaction
        return redirect(url_for('success_page'))
    else:
        return "Invalid ID", 400
    
@app.route('/register/manager', methods=['GET'])
def show_manager_registration_form():
    return render_template('reg_manager.html')

@app.route('/register/manager', methods=['POST'])
def register_manager():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    birthday = request.form['birthday']
    employee_id = request.form['employee_id']

    if validate_employee_id(employee_id, 'manager'):
        password_hash = generate_password_hash(password)
        # Implement the logic to save these details to your database
        return redirect(url_for('success_page'))
    else:
        return "Invalid ID", 400


def generate_employee_id(role):
    prefix = {'chef': 'C', 'delivery': 'D', 'food_importer': 'F', 'manager': 'M'}
    if role in prefix:
        return f"{prefix[role]}{random.randint(10000, 99999)}"
    return None

def validate_employee_id(id, role):
    pattern = {
        'chef': r'^C\d{5}$',
        'delivery': r'^D\d{5}$',
        'food_importer': r'^F\d{5}$',
        'manager': r'^M\d{5}$'
    }
    if role in pattern:
        return re.match(pattern[role], id) is not None
    return False

@app.route('/success')
def success_page():
    return "Registration Successful!"  # Or render a success template

@app.route('/register/customer', methods=['GET'])
def show_customer_registration_form():
    return render_template('reg_customer.html')

@app.route('/register/customer', methods=['POST'])
def register_customer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    birthday = request.form['birthday']

    password_hash = generate_password_hash(password)
    # Implement the logic to save these details to your database
    return redirect(url_for('customer_success_page'))

@app.route('/customer_success')
def customer_success_page():
    return render_template('customer_success.html')  # This template needs to be created


if __name__ == '__main__':
    app.run(debug=True, port=5002)
