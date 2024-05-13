from Order import Order
from Chef import Chef
import Database

# Creates inventory database and populates it
A = Database.Inventory()
A.addIngredient('Lettuce','Vegetable',2,'2024-06-20')
A.addIngredient('Lettuce','Vegetable',5,'2024-06-21')
A.addIngredient('Tomatoes','Vegetable',10,'2024-06-22')
A.addIngredient('Chicken','Meat',5,'2024-06-18')
A.addIngredient('Bread','Grain',1,'2024-06-30')
A.printTable()

# Creates Menu database and populates it
M = Database.Menu()
M.addDish('Salad',['Lettuce,Tomatoes'])
M.addDish('Sandwich',['Bread,Lettuce'])
M.printTable()

# Creates orders including one VIP Order
orderTest1 = Order(123, 'Sandwich')
orderTest2 = Order(124, 'Salad')
orderTestVIP = Order(125, 'Special Salad', specialOrder=True, ingredients=['Lettuce','Tomatoes','Chicken'])

# Creates Chefs to make the orders
chef1 = Chef('John Smith', 50000)
chef2 = Chef('Rosalyn Franklin', 50000)

# Runs validation of ingredients, adds to queue, and then distributes each order to an available chef
orderTest1.validateIngredientsAndAddToQueue()
orderTest1.distributeToChef()

orderTestVIP.validateIngredientsAndAddToQueue()
orderTestVIP.distributeToChef()

# Deletes database at the end (to refresh everything)
Database.delete_database(Database.create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud'),'CulinaryCloud')