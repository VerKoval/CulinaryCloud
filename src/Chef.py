from queue import Queue

# #   CHEF CHEF CHEF CHEF CHEF 
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

class Chef:

    def prepareOrder (self, orderQueue):

        """
        Chef Use Case 1
        """

        currentOrder = orderQueue.get()
        print(currentOrder)





# // Function to validate ingredients and add order to priority queue
# Function ValidateIngredientsAndAddToQueue(order)
#     Connect to Inventory Database
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

# // Function to distribute orders to chefs
# Function DistributeOrdersToChefs
#     While there are orders in the priority queue:
#         If there is an available chef:
#             order = priority queue.pop() // Removes the highest priority order
#             AssignOrderToChef(order, chef)
#         Else:
#             Break // Wait for a chef to become available

# // Function to assign order to a chef
# Function AssignOrderToChef(order, chef)
#     chef.startPreparation(order)
#     When chef indicates order is done:
#         MoveOrderToNextQueue(order) // E.g., to delivery queue
#         Display message "Order completed and moved to next queue"

# // Function to move completed order to another queue (like delivery)
# Function MoveOrderToNextQueue(order)
#     Add order to delivery queue


# #Use Case 2 (Special Order Handling):Pseudo code 
# # Classes and functions to handle special orders for VIP customers
# // Main Program
# Start Program
#     Listen for VIP customer requests
#     While request received:
#         HandleVIPSpecialOrder(request)
#     End While
# End Program

# // Function to handle special order requests from VIP customers
# Function HandleVIPSpecialOrder(request)
#     VIPCustomer = request.getCustomer()
#     specialMeal = VIPCustomer.requestMeal(request.getMealDetails())
#     If validateMeal(specialMeal):
#         AddMealToDatabase(specialMeal)
#         AddMealToPriorityQueue(specialMeal, VIPCustomer)
#         Display message "Special meal added to preparation queue and menu database"
#     Else:
#         Display message "Meal request cannot be processed"

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

# // Function to add the meal to the priority queue
# Function AddMealToPriorityQueue(meal, customer)
#     Connect to Order System
#     Determine priority based on customer status and meal specifics
#     Add meal to priority queue with determined priority
#     Close Connection




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


