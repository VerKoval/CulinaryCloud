from queue import Queue
from Database import Menu, Feedback

class Chef:

    currentChefID = 2000

    # Stores queue of all available and unavailable chefs
    chefAvailableQueue = Queue(maxsize = 10)
    chefUnavailableQueue = Queue(maxsize = 10)

    def __init__ (self, name, salary):
        
        # Adds instance variables
        Chef.currentChefID += 1
        self.ID = Chef.currentChefID
        self.name = name
        self.salary = salary

        # Adds chef to free chef queue upon creation
        Chef.chefAvailableQueue.put(self)

    def prepareOrder (self, orderQueue):

        """
        Chef Use Case 1: Preparing the order
        """

        if Chef.chefAvailableQueue.qsize() == 0:
            print('No available chefs to cook meal')
        
        else:

            # Gets the order and gets an available chef
            currentOrder = orderQueue.get()
            chefCookingOrder = Chef.chefAvailableQueue.get()

            # Also adds chef to unavailable queue
            Chef.chefUnavailableQueue.put(chefCookingOrder)

            print(f'Preparing: {currentOrder.dish} by Chef: {chefCookingOrder.name}')

    def raiseQualityIssue (self, accusedID, complaintText):

        """
        Use Case 3: Raises quality issue of the ingredients from the chef side
        """

        # Creates feedback database table and connection
        feedbackDB = Feedback()

        # Adds feedback using feedback function
        feedbackDB.addFeedback(self.ID, accusedID, 'IngredientQuality', complaintText)

    # def setCurrentMenu (self, menuItems):

    #     """
    #     Function that takes in a list of menu items and sets that as the current menu (one in use)
    #     """

    #     menuDB = Menu()

    #     for dish in menuItems:
    #         if menuDB.checkIfPresent(dish) == True:
    #             if menuDB.checkIfInUse(dish) == False:
    #                 Menu.addToCurrentDishes()
    #         else:
    #             print('Entered a dish that does not exist')
    #             return
                
    
# #Use Case 3 (Raise Quality Issue): Pseudo code  
# # Classes and functions to handle quality issues for a food importer
# // Main Program
# Start Program
#     Initialize complaints queue
#     While program is running:
#         Listen for new complaints
#         If new complaint received:
#             AddComplaintToQueue(newComplaint)
#         If management requests view:
#             DisplayComplaintsQueue()
#     End While
# End Program

# // Function to add a new complaint to the queue
# Function AddComplaintToQueue(complaint)
#     // Extract complaint details
#     complaintType = complaint.getType()
#     complaintSeverity = complaint.getSeverity()
#     complaintDate = GetCurrentDate()
#     // Create a structured complaint object
#     newComplaint = {
#         Type: complaintType,
#         Severity: complaintSeverity,
#         DateCreated: complaintDate
#     }
#     // Add the complaint to the queue with severity as priority
#     complaintsQueue.insertWithPriority(newComplaint, complaintSeverity)
#     Display message "Complaint added successfully with severity level: " + complaintSeverity

# // Function to display the complaints queue
# Function DisplayComplaintsQueue()
#     If complaintsQueue is not empty:
#         For each complaint in complaintsQueue:
#             Display "Type: " + complaint.Type
#             Display "Severity: " + complaint.Severity
#             Display "Date Created: " + complaint.DateCreated
#     Else:
#         Display "No current complaints."

# // Utility function to get current date
# Function GetCurrentDate()
#     // This would typically interface with the system's clock
#     Return system.currentDate()


# #Use Case 4 (Decide Menu): Pseudo code
# // Main Program
# Start Program
#     While program is running:
#         Display Chef Options:
#             1. Add New Dish
#             2. View Current Menu
#         Choose option:
#             If option 1:
#                 CreateNewDish()
#             If option 2:
#                 DisplayCurrentMenu()
# End Program

# // Function to create a new dish and update databases
# Function CreateNewDish
#     dishDetails = GetDishDetailsFromChef()
#     If not DishExistsInDatabase(dishDetails.name):
#         AddDishToDatabase(dishDetails)
#         For each ingredient in dishDetails.ingredients:
#             If not IngredientExistsInDatabase(ingredient):
#                 AddIngredientToDatabase(ingredient)
#         Display message "New dish and ingredients added to database"
#     Else:
#         Display message "Dish already exists in the database"

# // Function to display the current menu
# Function DisplayCurrentMenu
#     Connect to Database
#     Fetch all dishes from dishes table
#     For each dish in results:
#         Display dish.name + " - " + dish.description
#     Close Database Connection


