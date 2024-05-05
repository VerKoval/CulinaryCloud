from queue import Queue
import mysql.connector
from mysql.connector import Error
from Chef import Chef
from Database import Inventory

class Order:

    # Stores queue of all order objects that are created
    orderQueue = Queue(maxsize = 10)

    def __init__ (self, customerID, dishName, ingredients):

        # Sets instance variables
        self.customerID = customerID
        self.dish = dishName
        self.ingredients = ingredients

        # Checks if ingredients are present then adds to queue
        self.validateIngredientsAndAddToQueue()

    def validateIngredientsAndAddToQueue (self):

        """
        Check if ingredients are present and add to the order queues
        """

        # Checks if ingredients available
        if self.checkIngredientsAvailable(self.ingredients) == True:
            
            # Adds order object to the queue
            Order.orderQueue.put(self)
            print('Order added to preparation queue')

        else:
            print('Order cannot be processed due to lack of ingredients')


    def checkIngredientsAvailable (self, ingredientsList):
        
        """
        Function to check ingredient availability
        """

        # Creates Inventory Database connection object
        inventoryDB = Inventory()

        # Loops through each ingredient and checks if it is present
        for ingredient in ingredientsList:
            if inventoryDB.checkIfPresent(ingredient) == False:
                return False
        return True

    # def distributeToChef (self):


# # #   CHEF CHEF CHEF CHEF CHEF 

# # Use Case 1 (Prepare Order): Pseudo code// Main Program
# Start Program
#     Initialize priority queue for orders
#     While the restaurant is open:
#         Check for new orders
#         If new order received:
#             ValidateIngredientsAndAddToQueue(newOrder)
#         DistributeOrdersToChefs()
#     End While
# End Program

# Running code

# order1 = Order(123, 'Sandwich', ['Lettuce','Bread'])
# order2 = Order(124, 'Sandwich', ['Lettuce','Bread'])

# print(order1)
# print(order2)
# print(Order.orderQueue.qsize())

# Order.orderQueue.get()
# print(Order.orderQueue.qsize())

# Order.orderQueue.get()
# print(Order.orderQueue.qsize())

# connection = create_server_connection("localhost", "root", 'CSC322Wei')

# orderQueue = Queue(maxsize = 10)

# A = Chef()
# A.prepareOrder(orderQueue)

# B = Chef()
# B.prepareOrder(orderQueue)

# ingredientList = ['Lettuce','Bread']
# print(checkIngredientsAvailable(ingredientList))

