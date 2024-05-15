from queue import Queue
import mysql.connector
from mysql.connector import Error
from Chef import Chef
from Database import Customers, Menu, Feedback
from Order import Order

class Customer:

    cartQueue = Queue(maxsize = 50) #Just names of items being put in cart
    cartPrice = 0 #Total price of items in cart
    Cust = Customers()

    def __init__ (self, customerID, firstname, lastname, money, paymentInfo = 0, vip = False, warn=0, orders = 0):

        # Sets instance variables
        self.ID = customerID
        self.firstname = firstname
        self.lastname = lastname
        self.money = money
        self.payInfo = paymentInfo
        self.VIP = vip
        self.warnings = warn
        self.orders = orders

        #if two warnings, delete customer
        if self.warnings >= 2:
            if not self.VIP:
                Customer.remove()
            else:
                self.VIP = False
                Customer.Cust.demoteCustomer(self.ID)

        if not vip:
            if self.payInfo > 500 or self.orders > 50:
                self.VIP = True
                Customer.Cust.promoteCustomer(self.ID)

#place regular order
    def placeOrder(self, menuItem, checkout = False):
        if not Customer.Cust.checkCustomer(self.ID): return #checks if customer
        MenuDB = Menu()
        if MenuDB.checkIfPresent(menuItem) or not MenuDB.checkIfPresent(menuItem):
            discount = 0.9 if self.VIP else 1 #discount for vips
            Customer.cartPrice += discount*MenuDB.getPrice(menuItem)[0][0]
            Customer.cartQueue.put(menuItem)
            if checkout:
                Customer.checkout()

#process all items on queue and make the transaction
    def checkout(self):
        if not Customer.Cust.checkCustomer(self.ID): return
        while not Customer.cartQueue.empty():
            if Customer.cartPrice <= self.money:
                item = Customer.cartQueue.get()
                if item.endswith("special"):
                    order = Order(self.ID, item, specialOrder = True)
                else:
                    order = Order(self.ID, item)
                order.distributeToChef()
                self.money -= Customer.cartPrice
                Customer.Cust.addMoney(self.ID, -Customer.cartPrice)
                price = Customer.cartPrice
                Customer.cartPrice = 0
                return price
            else:
                print("add more money")
                break
    
    #allow customer to add money to their account
    def addMoney(self, add):
        if not Customer.Cust.checkCustomer(self.ID): return
        self.money += add
        Customer.Cust.addMoney(self.ID, add)

#delete customer from database
    def remove(self):
        if not Customer.Cust.checkCustomer(self.ID): return
        Customer.Cust.removeCustomer(self.ID)

#feedback
    def Complain (self, accusedID, complaintText):
        if not Customer.Cust.checkCustomer(self.ID): return
        # Creates feedback database table and connection
        feedbackDB = Feedback()

        # Adds feedback using feedback function
        feedbackDB.addFeedback(self.ID, accusedID, 'Customer Feedback', complaintText)
        if self.VIP:
            feedbackDB.addFeedback(self.ID, accusedID, 'Customer Feedback', complaintText) #vip feedback counted twice
    

    #Rate the food
    
    def giveRating (self, rating, item):
        if not Customer.Cust.checkCustomer(self.ID): return
        menu = Menu()
        menu.addRating(item, rating)

    #special food
    def exclusiveOffer(self, item, price):
        if not Customer.Cust.checkCustomer(self.ID): return
        item += "special"
        Customer.cartQueue.put(item)
        Customer.cartPrice += price

    #get number of items in cart
    def numCart(self):
        return Customer.cartQueue.qsize()
    
    #get number of items in cart
    def cartPrices(self):
        return Customer.cartPrice
    
    def addWarning(self):
        Customer.warnings += 1
        return Customer.warnings

 