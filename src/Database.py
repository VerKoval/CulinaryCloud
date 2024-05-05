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

    def checkIfPresent (self, ingredientName):

        """
        Function that checks if the ingredient is present in the database
        """

        # Query that tests whether a value is present in a database or not
        ingredientIsPresentString = f"""
            SELECT COUNT(1) 
            FROM Inventory
            WHERE name = '{ingredientName}';
            """
        
        ingredientIsPresent = self.execute_query(ingredientIsPresentString, returnFlag=True)

        # Returns False if the ingredient is not present, otherwise return True
        if ingredientIsPresent[0][0] == 0:
            return False
        else:
            return True

    def addIngredient (self, ingredientName, foodType, quantityToAdd, expirationDate):

        """
        Function that adds an ingredient into the Inventory database
        """

        # Checks if ingredient is present
        ingredientIsPresentFlag = self.checkIfPresent(ingredientName)

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

# Test running code 

# A = Inventory()

# A.addIngredient('Lettuce','Vegetable',2,'2024-06-20')
# A.addIngredient('Lettuce','Vegetable',5,'2024-06-21')
# A.addIngredient('Bread','Grain',1,'2024-06-30')
# print(A.checkIfPresent('Lettuce'))
# A.printTable()

# B = Inventory()

# Deletes database at the end
# delete_database(create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud'),'CulinaryCloud')

