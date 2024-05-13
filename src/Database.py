import mysql.connector
from mysql.connector import Error
from datetime import date

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

class Feedback (Database):

    currentFeedbackID = 0

    def __init__ (self):

        self.createTable()

    def createTable (self):

        """
        Function that creates table for Feedback
        """

        CreateTableFeedbackString = """
            CREATE TABLE IF NOT EXISTS Feedback (
            complaintID INT PRIMARY KEY,
            personComplainingID INT,
            personAccusedID INT,
            feedbackType VARCHAR(40),
            complaintDate DATE,
            complaintText TEXT(500)
            );
            """
        
        self.execute_query(CreateTableFeedbackString)

    def addFeedback (self, personComplainingID, personAccusedID, feedbackType, feedbackText):
        
        """
        Function that adds a given complaint or praise to the database
        """

        Feedback.currentFeedbackID += 1
        currentDate = date.today()

        insertFeedbackString = f"INSERT INTO Feedback VALUES ({Feedback.currentFeedbackID}, {personComplainingID}, {personAccusedID}, '{feedbackType}', '{currentDate}', '{feedbackText}');"
        self.execute_query(insertFeedbackString)

        self.printTable()

    def printTable (self):

        cursor = Database.connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM Feedback") 

        # fetch all the matching rows 
        result = cursor.fetchall() 
  
        # loop through the rows 
        for row in result: 
            print(row, '\n')