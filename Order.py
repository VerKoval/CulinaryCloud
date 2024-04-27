from queue import Queue
import mysql.connector
from mysql.connector import Error

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

def ValidateIngredientsAndAddToQueue (customerID, orderName, connection):

    #     If checkIngredientsAvailable(order):
    #         Add order to priority queue with appropriate priority
    #         Display message "Order added to preparation queue"
    #     Else:
    #         Display message "Order cannot be processed due to lack of ingredients"
    #     Close Database Connection

    # // Function to check ingredient availability
    # Function checkIngredientsAvailable(order)
    #     For each ingredient in order:
    #         If ingredient not in stock:
    #             Return false
    #     Return true
    orderQueue.put((customerID,orderName))

# Running code
# connection = create_server_connection("localhost", "root", 'CSC322Wei')



orderQueue = Queue(maxsize = 10)

A = Chef()
A.prepareOrder(orderQueue)

B = Chef()
B.prepareOrder(orderQueue)
