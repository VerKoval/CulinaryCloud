import random 
import bcrypt
import re
from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.security import generate_password_hash
import mysql.connector
from mysql.connector import Error
import Database
from Database import UserManagement
from Database import Menu
from Chef import Chef
from Order import Order
from flask_bcrypt import Bcrypt
 # app.py
from helpers import validate_employee_id
from Database import create_server_connection
import logging 


# Determine the absolute paths to the static and templates folders
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(project_root, 'static')
template_dir = os.path.join(project_root, 'templates')
# Assuming this is part of your main script or initialization routine
db_connection = create_server_connection("localhost", "root", 'CC14052024', 'CulinaryCloud')
user_management = UserManagement(db_connection)
user_management.create_user_table()  # Creates customer table
user_management.create_employee_table()  # Creates employee table
user_management.create_quality_issue_table()  # Creates quality issue table

# Initializes menu database connection object
menu_db = Menu()

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
bcrypt = Bcrypt(app)
user_management = UserManagement(db_connection)
app.config['SECRET_KEY'] = 'KEYCC14052024'

@app.route('/')
def front_page():
    return render_template('front_page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check hardcoded credentials
        if email == 'bellasmith1@gmail.com' and password == '12345':
            return redirect(url_for('customer_home_page'))  # Correct use of url_for
        elif email == 'davidyale@gmail.com' and password == 'david':
            return redirect(url_for('customer_home_page'))  # Correct use of url_for
        elif email == 'sn56@gmail.com' and password == 'nicks56':
            return redirect(url_for('food_importer_home_page'))
        elif email == 'clarabowts@gmail.com' and password == 'cbttpdts':
            return redirect(url_for('manager_home_page'))
        elif email == 'bobbyflay@gmail.com' and password == 'cooking':
            return redirect(url_for('chef_home_page'))
        else:
            return render_template('login.html', error="Invalid email or password. Please try again.")

    return render_template('login.html')

@app.route('/customer_home_page')
def customer_home_page():
    # This will render a generic customer home page
    return render_template('customer_home_page.html')

@app.route('/chef_home_page')
def chef_home_page():
    return render_template('chef_home_page.html')

@app.route('/foodimporter_home_page')
def food_importer_home_page():
    # This will render a specific page for food importers
    return render_template('foodimporter_home_page.html')


@app.route('/delivery_home_page')
def delivery_home_page():
    return render_template('delivery_home_page.html')

@app.route('/manager_home_page')
def manager_home_page():
    return render_template('manager_home_page.html')

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
        
        return redirect(url_for('chef_home_page'))
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
        return redirect(url_for('delivery_home_pag'))

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
        return redirect(url_for('food_importer_home_page'))

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
        return redirect(url_for('manager_home_page'))

    except Exception as e:
        # Catching and printing any errors that occur during registration
        print(f"Error during manager person registration: {e}")
        return str(e), 500

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
    return redirect(url_for('customer_home_page'))

@app.route('/surfer_menu_page')
def surfer_menu():
    return render_template('surfer_menu_page.html')

@app.route('/logout')
def logout():
    session.clear()  
    return redirect(url_for('front_page'))

@app.route('/manage_inventory')
def manage_inventory():
    # Fetch ingredients from your database or any other data source
    return render_template('manage_inventory.html')

@app.route('/raise_quality_f')
def raise_quality_f():
    return render_template('raise_quality_f.html')


@app.route('/raise_quality_issue', methods=['POST'])
def handle_quality_issue():
    description = request.form['description']
    reported_by = request.form['reported_by']
    date_reported = request.form['date_reported']

    # Ensure these are your correct credentials
    db_connection = create_server_connection("localhost", "actual_mysql_username", "actual_mysql_password", "CulinaryCloud")
    if db_connection is None:
        print("Failed to connect to database")
        return "Database connection error", 500

    user_manager = UserManagement(db_connection)
    user_manager.add_quality_issue(description, reported_by, date_reported)

    return redirect(url_for('foodimporter_home_page'))

@app.route('/manage_staff')
def manage_staff():
    connection = mysql.connector.connect(host='localhost', user='root', password='CC14052024', database='CulinaryCloud')
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('manage_staff.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    employee_id = request.form['employee_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    birthday = request.form['birthday']
    role = request.form['role']

    connection = mysql.connector.connect(host='localhost', user='root', password='CC14052024', database='CulinaryCloud')
    cursor = connection.cursor()
    query = """
    INSERT INTO Employees (employee_id, first_name, last_name, email, password, birthday, role)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (employee_id, first_name, last_name, email, password, birthday, role)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('manage_staff'))

@app.route('/manage_customers')
def manage_customers():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='CC14052024',
        database='CulinaryCloud'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Customers")  # Adjust the table name and columns as necessary
    customers = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('manage_customers.html', customers=customers)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    birthday = request.form['birthday']

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='CC14052024',
        database='CulinaryCloud'
    )
    cursor = connection.cursor()
    query = """
    INSERT INTO Customers (first_name, last_name, email, password, birthday)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (first_name, last_name, email, password, birthday)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('manage_customers'))

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def show_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='CC14052024',
        database='CulinaryCloud'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM FoodInventory")
    ingredients = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('manage_inventory.html', ingredients=ingredients)

@app.route('/add', methods=['POST'])
def add_ingredient():
    name = request.form.get('name')
    type = request.form.get('type')
    shipment_date = request.form.get('shipment_date')
    expiration_date = request.form.get('expiration_date')
    count = request.form.get('count')

    logging.debug(f"Form Data: name={name}, type={type}, shipment_date={shipment_date}, expiration_date={expiration_date}, count={count}")

    # Validate that required fields are not empty
    if not name or not type or not shipment_date or not expiration_date or not count:
        logging.error("Error: All fields are required")
        return render_template('manage_inventory.html', error="All fields are required")

    # Ensure count is a valid integer
    try:
        count = int(count)
    except ValueError:
        logging.error("Error: Count must be a valid integer")
        return render_template('manage_inventory.html', error="Count must be a valid integer")

    # Validate date format
    try:
        from datetime import datetime
        datetime.strptime(shipment_date, '%Y-%m-%d')
        datetime.strptime(expiration_date, '%Y-%m-%d')
    except ValueError:
        logging.error("Error: Invalid date format")
        return render_template('manage_inventory.html', error="Invalid date format")

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='CC14052024',
            database='CulinaryCloud'
        )
        cursor = connection.cursor()
        query = """
        INSERT INTO FoodInventoryI (item_name, quantity, unit, expiration_date)
        VALUES (%s, %s, %s, %s)
        """
        values = (name, count, type, expiration_date)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        logging.error(f"Database error: {err}")
        return render_template('manage_inventory.html', error=f"Database error: {err}")

    return redirect(url_for('show_database'))

@app.route('/view_menu')
def view_menu():

    # Actual running code
    menuItems = menu_db.getDishes()
    return render_template('view_menu.html', menuItems=menuItems)

@app.route('/add_dish', methods=('GET', 'POST'))
def add_dish():
    return render_template('add_dish.html')

@app.route('/add_dish_button', methods=('GET','POST'))
def add_dish_button():
    dishName = request.form['dishName']
    ingredientsList = request.form['ingredientsList']
    price = request.form['price']

    ingredientsList = ingredientsList.split(',')

    menu_db.addDish(dishName, ingredientsList, price)
    menu_db.printTable()
    print(f'Successfully added: {dishName}')

    return redirect(url_for('chef_home_page'))

@app.route('/process_order', methods=('GET', 'POST'))
def process_order():

    # # Creates inventory database and populates it
    # A = Database.Inventory()
    # A.addIngredient('Lettuce','Vegetable',2,'2024-06-20')
    # A.addIngredient('Lettuce','Vegetable',5,'2024-06-21')
    # A.addIngredient('Tomatoes','Vegetable',10,'2024-06-22')
    # A.addIngredient('Chicken','Meat',5,'2024-06-18')
    # A.addIngredient('Bread','Grain',1,'2024-06-30')
    # A.printTable()

    # # Creates Menu database and populates it
    # M = Database.Menu()
    # M.addDish('Salad',['Lettuce,Tomatoes'], 10)
    # M.addDish('Sandwich',['Bread,Lettuce'], 15)
    # M.printTable()

    # orderTest1 = Order(123, 'Sandwich')
    # orderTest2 = Order(124, 'Salad')
    # orderTestVIP = Order(125, 'Special Salad', specialOrder=True, specialIngredients=['Lettuce','Tomatoes','Chicken'], specialPrice=30)

    # orderTest1.validateIngredientsAndAddToQueue()
    # orderTest2.validateIngredientsAndAddToQueue()
    # orderTestVIP.validateIngredientsAndAddToQueue()

    orders = []
    for item in Order.orderQueue.queue:
        orders.append(item)

    print(orders)
    print(list(Order.orderQueue.queue))

    return render_template('process_order.html', orders=orders)

@app.route('/process_order_button', methods=('GET','POST'))
def process_order_button():

    chef = Chef('Bobby Flay',50000)
    chef.prepareOrder(Order.orderQueue)

    return redirect(url_for('chef_home_page'))

@app.route('/set_menu', methods=('GET', 'POST'))
def set_menu():
    return render_template('set_menu.html')

@app.route('/set_menu_button', methods=('GET','POST'))
def set_menu_button():

    dish1 = request.form['dishName1']
    dish2 = request.form['dishName2']
    dish3 = request.form['dishName3']
    dish4 = request.form['dishName4']
    dish5 = request.form['dishName5']

    menu_db.addToCurrentDishes(dish1)
    menu_db.addToCurrentDishes(dish2)
    menu_db.addToCurrentDishes(dish3)
    menu_db.addToCurrentDishes(dish4)
    menu_db.addToCurrentDishes(dish5)
    menu_db.printTable()

    return redirect(url_for('chef_home_page'))

@app.route('/delivery_orders')
def delivery_orders():
    return render_template('delivery_orders.html')

@app.route('/delivery_history')
def delivery_history():
    return render_template('delivery_history.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
