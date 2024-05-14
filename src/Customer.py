from queue import Queue
import mysql.connector
from mysql.connector import Error
from Chef import Chef
from Database import Customers, Menu, Feedback
from Order import Order

class Customers:

    # Stores queue of all order objects that are created
    cartQueue = Queue(maxsize = 10)
    cartPrice = 0
    Cust = Customers()

    def __init__ (self, customerID, firstname, lastname, money, paymentInfo = 0, vip = False, warn=0, orders = 0, pressRatings = False):

        # Sets instance variables
        self.ID = customerID
        self.firstname = firstname
        self.lastname = lastname
        self.money = money
        self.payInfo = paymentInfo
        self.VIP = vip
        self.warnings = warn
        self.orders = orders

        if warn == 2:
            if not vip:
                Customers.remove()
            else:
                vip = False
                Customers.Cust.demoteCustomer(self.ID)

        if not vip:
            if self.payInfo > 500 or self.orders > 50:
                vip = True
                Customers.Cust.promoteCustomer(self.ID)

    def placeOrder(self, menuItem, checkout = False):
        MenuDB = Menu()
        if MenuDB.checkIfPresent(menuItem):
            discount = 0.9 if self.VIP else 1 #discount for vips
            Customers.cartPrice += discount*MenuDB.getPrice(menuItem)
            Customers.cartQueue.put(menuItem)
            if checkout:
                Customers.checkout()

    def checkout(self):
        while not Customers.cartQueue.empty():
            if Customers.cartPrice <= self.money:
                item = Customers.cartQueue.get()
                order = Order(self.ID, item)
                order.distributeToChef()
                self.money -= Customers.cartPrice
                Customers.Cust.addMoney(self.ID, -Customers.cartPrice)
                return Customers.cartPrice
    
    def addMoney(self, add):
        self.money += add
        Customers.Cust.addMoney(self.id, add)

    def remove(self):
        Customers.Cust.removeCustomer(self.ID)

    def raiseQualityIssue (self, accusedID, complaintText):

        # Creates feedback database table and connection
        feedbackDB = Feedback()

        # Adds feedback using feedback function
        feedbackDB.addFeedback(self.ID, accusedID, 'Customer Comment', complaintText)
        if self.VIP:
            feedbackDB.addFeedback(self.ID, accusedID, 'Customer Comment', complaintText) #vip feedback counted twice

    







        



        

#Use Case 1 (Common to customers and surfers/ view menu): Pseudo code
"""
// Main program
Start Program
    Show Main Menu
    Choose option:
        1. View Menu
        2. View Ratings
    If option 1:
        ViewMenu()
    If option 2:
        ViewRatings()
End Program

// Function to view the menu
Function ViewMenu
    Connect to Database
    Fetch dishes where attribute 'currently making' is true
    For each dish in result
        Display dish name
        On user action, display dropdown menu:
            Show ingredients
            Show calories
    Close Database Connection

// Function to view ratings
Function ViewRatings
    Connect to Database
    Fetch ratings for the restaurant
    If ratings available:
        Display histogram of overall restaurant ratings
        Ask user if they want to see individual dish ratings
        If yes:
            For each dish in database
                Display dish name
                Fetch and show histogram of ratings for the dish
    Else:
        Display message "No ratings available"
    Close Database Connection



#Use Case 2 (Only customers use case ): Pseudo code
// Main Program
Start Program
    Show Customer Menu
    Choose option:
        1. Place Order
        2. View Cart and Checkout
    If option 1:
        PlaceOrder()
    If option 2:
        Checkout()
End Program

// Function to place an order
Function PlaceOrder
    Connect to Database
    Fetch menu items that are 'currently making'
    Display menu items
    Initialize cart (implement as Stack)
    While user wants to add items:
        Get user selection
        Push selected item to cart
        Ask if user wants to add more items
    Display message "Items added to cart"
    Close Database Connection

// Function to checkout
Function Checkout
    If cart is not empty:
        Display all items in cart
        Ask user to confirm the order
        If confirmed:
            Move items from cart to chef's meal preparation queue
            Display message "Order placed successfully!"
        Else:
            Display message "Checkout cancelled"
    Else:
        Display message "Cart is empty"


#Use Case 3 (only VIP customers use case): Pseudo code
// Main Program
Start Program
    Show VIP Customer Menu
    Choose option:
        1. Access Exclusive Offers
        2. Make Special Food Request
    If option 1:
        AccessOffers()
    If option 2:
        SpecialFoodRequest()
End Program

// Function to access exclusive offers
Function AccessOffers
    Connect to Database
    Fetch exclusive offers
    Display offers
    Initialize cart (implement as Stack if not already initialized)
    While user wants to add offers:
        Get user selection of offer
        Add offer to cart with negative value (discount)
        Ask if user wants to add more offers
    Display message "Offers added to cart"
    Close Database Connection

// Function to make a special food request
Function SpecialFoodRequest
    Display special request menu form with text and sub-text fields for ingredients
    User fills in the details
    Connect to Database
    Check if ingredients are available
    If all ingredients available:
        Add special request to cart
        Add request to chef's queue of incoming orders
        Display message "Special request placed successfully!"
    Else:
        Display message "Ingredients not available for your request"
    Close Database Connection"""