from queue import Queue
import mysql.connector
from mysql.connector import Error
from Chef import Chef
from Database import Inventory, Menu

class Order:

    # Stores queue of all order objects that are created
    orderQueue = Queue(maxsize = 10)

    def __init__ (self, customerID, dishName, specialIngredients=None, specialPrice=None, specialOrder=False):

        # Sets instance variables
        self.customerID = customerID
        self.dish = dishName
        self.specialOrder = specialOrder

        # Checks if special order, if so then uses the ingredients provided
        # If not a special order then it uses the ingredients stored in the Menu database for that dish
        menuDB = Menu()
        
        if specialOrder == True:
            self.ingredients = specialIngredients
            self.price = specialPrice
        else:
            if menuDB.checkIfPresent(dishName) == True:
                self.ingredients = menuDB.getIngredients(dishName)
            else:
                print('Dish does not exist')

            self.price = menuDB.getPrice(dishName)

    def validateIngredientsAndAddToQueue (self):

        """
        Check if ingredients are present and add to the order queues
        """

        # Creates Inventory Database connection object
        inventoryDB = Inventory()

        # Checks if ingredients available
        if inventoryDB.checkIfPresent(self.ingredients) == True:

            # If it is a special order then add the meal to database
            if self.specialOrder == True:
                self.addMealToDatabase()
                print('Added special meal to database')
            
            # Adds order object to the queue
            Order.orderQueue.put(self)
            print('Order added to preparation queue')

        else:
            print('Order cannot be processed due to lack of ingredients')

    def distributeToChef (self):

        """
        Function that distributes order to an available Chef
        """

        Chef.prepareOrder(self, Order.orderQueue)

    def addMealToDatabase (self):

        """
        Function that adds a new meal to the database if this is a special order
        """

        # Creates Menu Database connection object
        menuDB = Menu()

        # Adds dish to the Menu database
        menuDB.addDish(self.dish,self.ingredients,self.price)

