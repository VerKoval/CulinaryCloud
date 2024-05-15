from Customer import Customer
import Database

# Creates inventory database and populates it
A = Database.Customers()
A.addCustomer('Kelly','Banks','kelly@example.com', 'password1', '1973-05-14',400,200,False,0, 51)
A.addCustomer('Roy','Howard','roy@example.com', 'password2', '1982-08-22',700,200,True,2,100)
A.addCustomer('Jay','Cobb','jay@example.com', 'password3', '1982-12-22')
A.printTable()

Jay = Customer(*A.getInfo(1))
Roy = Customer(*A.getInfo(3))
Kelly = Customer(*A.getInfo(4))


# Sample menu
M = Database.Menu()
M.printTable()

#Place order, doesn't have enough money, add money, checkout
Jay.placeOrder('Salad')
Jay.placeOrder('Sandwich')
Jay.cartPrices()
print(Jay.checkout())
Jay.addMoney(100)
Jay.checkout()

#She should be promoted to VIP automatically because of her stats
print("Kelly is a VIP is", {Kelly.VIP})




# # Deletes database at the end (to refresh everything)
# Database.delete_database(Database.create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud'),'CulinaryCloud')