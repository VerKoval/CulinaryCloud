import random 
import bcrypt
import re
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.security import generate_password_hash
import mysql.connector
from mysql.connector import Error
import Database
from Database import UserManagement
from Database import Menu
from flask_bcrypt import Bcrypt
 # app.py
from helpers import validate_employee_id
from Database import create_server_connection


# Determine the absolute paths to the static and templates folders
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(project_root, 'static')
template_dir = os.path.join(project_root, 'templates')
# Assuming this is part of your main script or initialization routine
db_connection = create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud')
user_management = UserManagement(db_connection)
user_management.create_user_table()  # Creates customer table
user_management.create_employee_table()  # Creates employee table

# Initializes menu database connection object
menu_db = Menu()


app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
bcrypt = Bcrypt(app)
user_management = UserManagement(db_connection)

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
    print("Registering chef...")
    try:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthday']
        
        print(f"Received data: {first_name}, {last_name}, {email}")

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        employee_id = request.form['employee_id'] 

        user_management.add_employee(first_name, last_name, email, password_hash, birthday, role='chef', employee_id=employee_id)
        
        return redirect(url_for('success_page'))
    except Exception as e:
        print(f"Error during chef registration: {e}")
        return str(e), 500

    
    # New routes for delivery registration
@app.route('/register/delivery', methods=['GET'])
def show_delivery_registration_form():
    return render_template('reg_delivery.html')

@app.route('/register/delivery', methods=['POST'])
def register_delivery():
    print("Registering delivery person...")
    try:
        # Extracting form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthday']

        # Logging received data for debugging
        print(f"Received data: {first_name}, {last_name}, {email}")

        # Generating a password hash
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # Assuming employee_id is submitted via form, otherwise generate as needed
        employee_id = request.form['employee_id'] 

        # Add the new employee to the database via your user management system
        user_management.add_employee(first_name, last_name, email, password_hash, birthday, role='delivery', employee_id=employee_id)

        # Redirect to a success page after registration
        return redirect(url_for('success_page'))

    except Exception as e:
        # Catching and printing any errors that occur during registration
        print(f"Error during delivery person registration: {e}")
        return str(e), 500  

@app.route('/register/importer', methods=['GET'])
def show_importer_registration_form():
    return render_template('reg_food_importer.html')

@app.route('/register/food_importer', methods=['POST'])
def register_importer():
    print("Registering importer person...")
    try:
        # Extracting form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthday']
        employee_id = request.form['employee_id'] 

        # Logging received data for debugging
        print(f"Received data: {first_name}, {last_name}, {email}")

        # Generating a password hash
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # Validating employee ID
        if not validate_employee_id('food_importer', employee_id):
            raise ValueError("provided employee ID is invalid.")

        # Add the new employee to the database
        user_management.add_employee(first_name, last_name, email, password_hash, birthday, role='food_importer', employee_id=employee_id)

        # Redirect to a success page after registration
        return redirect(url_for('success_page'))

    except Exception as e:
        # Catching and printing any errors that occur during registration
        print(f"Error during importer person registration: {e}")
        return str(e), 500
    
@app.route('/register/manager', methods=['GET'])
def show_manager_registration_form():
    return render_template('reg_manager.html')

@app.route('/register/manager', methods=['POST'])
def register_manager():
    print("Registering manager person...")
    try:
        # Extracting form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        birthday = request.form['birthday']

        # Logging received data for debugging
        print(f"Received data: {first_name}, {last_name}, {email}")

        # Generating a password hash
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        # Assuming employee_id is submitted via form, otherwise generate as needed
        employee_id = request.form['employee_id'] 

        # Add the new employee to the database via your user management system
        user_management.add_employee(first_name, last_name, email, password_hash, birthday, role='manager', employee_id=employee_id)

        # Redirect to a success page after registration
        return redirect(url_for('success_page'))

    except Exception as e:
        # Catching and printing any errors that occur during registration
        print(f"Error during manager person registration: {e}")
        return str(e), 500

@app.route('/success')
def success_page():
    return "Registration Successful!"  # Or render a success template

@app.route('/register/customer', methods=['GET'])
def show_customer_registration_form():
    print("Loading customer registration form")
    return render_template('reg_customer.html')

@app.route('/register/customer', methods=['POST'])
def register_customer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    birthday = request.form['birthday']
    
    # Generate password hash using Flask-Bcrypt
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # Add customer to user management
    user_management.add_customer(first_name, last_name, email, password_hash, birthday)
    
    # Redirect to customer success page
    return redirect(url_for('customer_success_page'))

@app.route('/customer_success')
def customer_success_page():
    return render_template('customer_success.html')

@app.route('/view_menu')
def view_menu():

    # Creates Menu database and populates it
    M = Menu()
    M.addDish('Salad',['Lettuce,Tomatoes'], 10)
    M.addDish('Sandwich',['Bread,Lettuce'], 15)
    M.printTable()

    # menuItems = ['Sandwich']
    # chef1.setCurrentMenu(menuItems)

    # Actual running code
    menuItems = menu_db.getDishes()
    print(menuItems)
    return render_template('view_menu.html', menuItems=menuItems)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
