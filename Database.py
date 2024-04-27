import mysql.connector
from mysql.connector import Error

def create_database(connection, db_name):

    """
    Function that creates the CulinaryCloud database
    """

    cursor = connection.cursor()
    try:
        cursor.execute(f'CREATE DATABASE {db_name}; \n USE {db_name}')
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

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
            passwd=user_password,
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

# Deletes database at the end
delete_database(create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud'),'CulinaryCloud')

