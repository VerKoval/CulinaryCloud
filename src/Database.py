import mysql.connector
from mysql.connector import Error
# app.py
from helpers import validate_employee_id




def create_database(connection, db_name):
    cursor = connection.cursor()
    cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
    result = cursor.fetchone()
    if not result:
        cursor.execute(f"CREATE DATABASE {db_name};")
        print("Database created successfully")
    else:
        print("Database already exists")

def delete_database(connection, db_name):

    """
    Function that deletes the CulinaryCloud database
    """

    cursor = connection.cursor()
    try:
        cursor.execute(f'DROP DATABASE {db_name};')
        print("Database dropped successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_server_connection(host_name, user_name, user_password, db_name=None):

    """
    Function that establishes the connection to the SQL database
    """

    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd= 'CC14052024',
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

class Database:

    # Creates class variables regarding the database and connection to SQL
    connection = create_server_connection("localhost", "root", 'CSC322Wei')
    database = create_database(connection, 'CulinaryCloud')
    connection = create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud')

    def execute_query(self, query):

        """
        Function that broadly executes query
        """

        cursor = Database.connection.cursor()
        try:
            cursor.execute(query)
            Database.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

class Inventory (Database):

    def createTable (self):

        """
        Function that creates table for the Inventory
        """

        CreateTableInventoryString = """
            CREATE TABLE Inventory (
            name CHAR(16) PRIMARY KEY,
            foodType VARCHAR(40),
            stockQuantity INT,
            expirationDate DATE
            );
            """
        
        self.execute_query(CreateTableInventoryString)

# Test running code 

A = Inventory()
A.createTable()
print(A.connection)

B = Inventory()
print(B.connection)

class UserManagement(Database):

    def __init__(self, db_connection):
        self.connection = db_connection

    def create_user_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            password VARCHAR(255),
            birthday DATE
        );
        """
        self.execute_query(create_table_query)
        print("Customer table created successfully")

    def create_employee_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Employees (
            employee_id VARCHAR(6) PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            password VARCHAR(255),
            birthday DATE,
            role VARCHAR(50)
        );
        """
        self.execute_query(create_table_query)
        print("Employee table created successfully")

    def add_customer(self, first_name, last_name, email, password_hash, birthday):
        add_customer_query = f"""
        INSERT INTO Customers (first_name, last_name, email, password, birthday) 
        VALUES ('{first_name}', '{last_name}', '{email}', '{password_hash}', '{birthday}');
        """
        self.execute_query(add_customer_query)
        print("Customer added successfully")

    def add_employee(self, first_name, last_name, email, password_hash, birthday, role, employee_id):
        if not validate_employee_id(role, employee_id):
            raise ValueError("provided employee ID is invalid.")
        
        add_employee_query = f"""
        INSERT INTO Employees (employee_id, first_name, last_name, email, password, birthday, role) 
        VALUES ('{employee_id}', '{first_name}', '{last_name}', '{email}', '{password_hash}', '{birthday}', '{role}');
        """
        self.execute_query(add_employee_query)
        print("Employee added successfully")

def execute_query(self, query):
    cursor = Database.connection.cursor()
    try:
        cursor.execute(query)
        Database.connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error during query execution: {err}")
        raise



# Deletes database at the end
#delete_database(create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud'),'CulinaryCloud')
