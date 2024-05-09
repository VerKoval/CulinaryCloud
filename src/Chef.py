from queue import Queue

class Chef:

    # Stores queue of all available and unavailable chefs
    chefAvailableQueue = Queue(maxsize = 10)
    chefUnavailableQueue = Queue(maxsize = 10)

    def __init__ (self, ID, name, salary):
        
        # Adds instance variables
        self.ID = ID
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



# // Function to validate the meal details
# Function validateMeal(meal)
#     // Example validation checks might include ingredient availability or recipe integrity
#     If meal has all necessary details and ingredients are available:
#         Return true
#     Return false

# // Function to add the meal to the restaurant's dishes database
# Function AddMealToDatabase(meal)
#     Connect to Database
#     Add meal to dishes table
#     Close Database Connection



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

# // Function to add dish to the dishes database
# Function AddDishToDatabase(dish)
#     Connect to Database
#     Insert dish into dishes table
#     Close Database Connection

# // Function to add ingredient to the ingredients database
# Function AddIngredientToDatabase(ingredient)
#     Connect to Database
#     Insert ingredient into ingredients table
#     Close Database Connection

# // Function to check if a dish already exists in the database
# Function DishExistsInDatabase(dishName)
#     Connect to Database
#     Search for dish by name in dishes table
#     If dish found:
#         Return true
#     Return false

# // Function to check if an ingredient already exists in the database
# Function IngredientExistsInDatabase(ingredientName)
#     Connect to Database
#     Search for ingredient by name in ingredients table
#     If ingredient found:
#         Return true
#     Return false

# // Function to display the current menu
# Function DisplayCurrentMenu
#     Connect to Database
#     Fetch all dishes from dishes table
#     For each dish in results:
#         Display dish.name + " - " + dish.description
#     Close Database Connection


