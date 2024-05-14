import mysql.connector
from mysql.connector import Error
from helpers import validate_employee_id
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
            passwd='CC14052024',
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

class Database:

    # Creates class variables regarding the database and connection to SQL
    connection = create_server_connection("localhost", "root", 'CC14052024')
    database = create_database(connection, 'CulinaryCloud')
    connection = create_server_connection("localhost", "root", 'CC14052024', 'CulinaryCloud')

    def execute_query(self, query, returnFlag=False):

        """
        Function that broadly executes query
        Specify returnFlag to be True if you want to return a value from SQL
        """

        cursor = Database.connection.cursor(buffered=True)

        try:
            cursor.execute(query)
            Database.connection.commit()
            print("Query successful")

            if returnFlag == True:
                myresult = cursor.fetchall()
                return myresult

        except Error as err:
            print(f"Error: '{err}'")

class Inventory (Database):

    def __init__ (self):

        self.createTable()
      
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

    def checkIfPresent (self, ingredientsList):

        """
        Function that checks if the ingredient is present in the database
        """

        for ingredientName in ingredientsList:

            # Query that tests whether a value is present in a database or not
            ingredientIsPresentString = f"""
                SELECT COUNT(1) 
                FROM Inventory
                WHERE name = '{ingredientName}';
                """
            
            ingredientIsPresent = self.execute_query(ingredientIsPresentString, returnFlag=True)

            # Returns False if the ingredient is not present
            if ingredientIsPresent[0][0] == 0:
                return False
            
        return True

    def addIngredient (self, ingredientName, foodType, quantityToAdd, expirationDate):

        """
        Function that adds an ingredient into the Inventory database
        """

        # Checks if ingredient is present
        ingredientIsPresentFlag = self.checkIfPresent([ingredientName])

        # If ingredient is present (value is False/0), then just update count
        if ingredientIsPresentFlag == True:
            updateIngredientString = f"""
                                    UPDATE Inventory
                                    SET stockQuantity = stockQuantity + {quantityToAdd}
                                    WHERE name = '{ingredientName}';
                                    """
            
            self.execute_query(updateIngredientString)
        
        # If ingredient is not present, add new ingredient in
        else:
            insertIngredientString = f"INSERT INTO Inventory VALUES ('{ingredientName}', '{foodType}', {quantityToAdd}, '{expirationDate}');"
            self.execute_query(insertIngredientString)

    def printTable (self):

        cursor = Database.connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM Inventory") 

        # fetch all the matching rows 
        result = cursor.fetchall() 
  
        # loop through the rows 
        for row in result: 
            print(row, '\n') 

class Menu (Database):

    def __init__ (self):

        self.createTable()

    def createTable (self):

        """
        Function that creates table for the Menu
        """

        CreateTableMenuString = """
            CREATE TABLE Menu (
            dish CHAR(16) PRIMARY KEY,
            ingredientsList VARCHAR(40),
            inUse INT
            );
            """
        
        self.execute_query(CreateTableMenuString)

    def checkIfPresent (self, dishName):

        """
        Function that checks if the dish is present in the database
        """

        # Query that tests whether a value is present in a database or not
        dishIsPresentString = f"""
            SELECT COUNT(1) 
            FROM Menu
            WHERE dish = '{dishName}';
            """
        
        dishIsPresent = self.execute_query(dishIsPresentString, returnFlag=True)

        # Returns False if the ingredient is not present, otherwise return True
        if dishIsPresent[0][0] == 0:
            return False
        else:
            return True

    def addDish (self, dishName, ingredientsList):

        """
        Function that adds a dish to the Menu database
        """

        # Creates list of ingredients as string to store in database
        ingredientsListString = ''
        for ingredient in ingredientsList:
            ingredientsListString += f'{ingredient},'
        
        insertIngredientString = f"INSERT INTO Menu VALUES ('{dishName}', '{ingredientsListString}', 1);"
        self.execute_query(insertIngredientString)

    def removeFromCurrentDishes (self, dishName):

        """
        Removes dish from current dishes that are in use
        """

        updateInUseString = f"""
                            UPDATE Menu
                            SET inUse = 0
                            WHERE dish = '{dishName}';
                            """
            
        self.execute_query(updateInUseString)

    def addToCurrentDishes (self, dishName):

        """
        Adds dish to current dishes that are in use
        """

        updateInUseString = f"""
                            UPDATE Menu
                            SET inUse = 1
                            WHERE dish = '{dishName}';
                            """
            
        self.execute_query(updateInUseString)

    def getIngredients (self, dishName):

        """
        Function that retrieves the ingredients list for a particular menu item
        """

        getIngredientsString = f"""
                            SELECT ingredientsList
                            FROM Menu
                            WHERE dish = '{dishName}';
                            """
        
        ingredientsList = self.execute_query(getIngredientsString, returnFlag=True)[0][0]
        ingredientsList = ingredientsList.split(',')
        ingredientsList.remove('')

        return ingredientsList

    def printTable (self):

        cursor = Database.connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM Menu") 

        # fetch all the matching rows 
        result = cursor.fetchall() 
  
        # loop through the rows 
        for row in result: 
            print(row, '\n') 
          
class UserManagement(Database):

    def __init__(self, db_connection):
        self.connection = db_connection

    def get_user_role(self, email, password):
        """
        Function that retrieves the role of a user based on their email and password.
        """
        try:
            cursor = self.connection.cursor()
            query = f"""
            SELECT role FROM Employees WHERE email = '{email}' AND password = '{password}';
            """
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the role if the user exists
            else:
                return None  # Return None if user not found or credentials don't match
        except Error as err:
            print(f"Error during role retrieval: {err}")
            return None

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
    def create_quality_issue_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS QualityIssues (
            issue_id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT,
            reported_by VARCHAR(255),
            date_reported DATE,
            status VARCHAR(50) DEFAULT 'Open'
        );
        """
        self.execute_query(create_table_query)
        print("Quality issue table created successfully")


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

def add_quality_issue(self, description, reported_by, date_reported):
    add_issue_query = """
    INSERT INTO QualityIssues (description, reported_by, date_reported) 
    VALUES (%s, %s, %s);
    """
    data = (description, reported_by, date_reported)
    self.execute_query(add_issue_query, data)
    print("Quality issue added successfully")

def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error during query execution: {err}")
            raise

def get_all_employees(self):
    try:
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Employees")
            return cursor.fetchall()
    except Exception as e:
        print("Error fetching employees:", e)
        return []

# Deletes database at the end
#delete_database(create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud'),'CulinaryCloud')
