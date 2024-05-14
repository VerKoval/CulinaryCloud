from Chef import Chef
import Database

chef1 = Chef('John Smith', 50000)
chef2 = Chef('Rosalyn Franklin', 50000)

# Creates Menu database and populates it
M = Database.Menu()
M.addDish('Salad',['Lettuce,Tomatoes'], 10)
M.addDish('Sandwich',['Bread,Lettuce'], 15)
M.printTable()

menuItems = ['Sandwich']
chef1.setCurrentMenu(menuItems)

M.printTable()

# Deletes database at the end (to refresh everything)
Database.delete_database(Database.create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud'),'CulinaryCloud')