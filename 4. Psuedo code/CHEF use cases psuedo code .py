#   CHEF CHEF CHEF CHEF CHEF 
# Use Case 1 (Prepare Order): Pseudo code
class Order:
    def __init__(self, order_id, meal, priority):
        self.order_id = order_id
        self.meal = meal
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        # Insert order by priority
        self.queue.append(order)
        self.queue.sort(key=lambda x: x.priority, reverse=True)

    def dequeue(self):
        # Remove the highest priority order
        return self.queue.pop(0) if self.queue else None

class InventoryDatabase:
    inventory = {'chicken': 10, 'rice': 20, 'veggies': 15}

    def check_ingredients(self, ingredients):
        # Check if ingredients are available in the inventory
        return all(self.inventory.get(item, 0) >= quantity for item, quantity in ingredients.items())

    def use_ingredients(self, ingredients):
        # Deduct used ingredients from the inventory
        for item, quantity in ingredients.items():
            if self.inventory.get(item, 0) >= quantity:
                self.inventory[item] -= quantity

class Chef:
    def __init__(self, name):
        self.name = name

    def prepare_order(self, order, inventory_db):
        # Check if ingredients are available
        if inventory_db.check_ingredients(order.meal['ingredients']):
            # Prepare the meal
            print(f"{self.name} is preparing {order.meal['name']}")
            inventory_db.use_ingredients(order.meal['ingredients'])
            print(f"{self.name} has finished preparing {order.meal['name']}")
            return True
        else:
            print(f"Not enough ingredients for {order.meal['name']}")
            return False

# Example usage
order_queue = PriorityQueue()
inventory_db = InventoryDatabase()
chef = Chef("Chef Gordon")

# Adding orders to the queue
order_queue.enqueue(Order(1, {'name': 'Chicken Rice', 'ingredients': {'chicken': 1, 'rice': 1}}, 5))
order_queue.enqueue(Order(2, {'name': 'Veggie Stir Fry', 'ingredients': {'veggies': 3}}, 3))

# Chef prepares the order
next_order = order_queue.dequeue()
if next_order:
    if chef.prepare_order(next_order, inventory_db):
        print(f"Order {next_order.order_id} prepared and is ready for next step")
    else:
        print(f"Order {next_order.order_id} could not be prepared due to ingredient shortage")

#Use Case 2 (Special Order Handling):Pseudo code 
# Classes and functions to handle special orders for VIP customers

class VIPCustomer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def request_special_order(self, meal_name, meal_ingredients):
        # VIP customer requests a special meal
        print(f"{self.name} has requested a special meal: {meal_name}")
        return {'name': meal_name, 'ingredients': meal_ingredients}

class MenuDatabase:
    # Database of all dishes the restaurant prepares
    menu_items = {}

    def add_to_menu(self, meal_name, meal):
        # Add a new meal to the menu database
        if meal_name not in self.menu_items:
            self.menu_items[meal_name] = meal
            print(f"New dish added to the menu: {meal_name}")
        else:
            print(f"Dish {meal_name} is already on the menu")

class KitchenOrderQueue:
    # Priority queue for managing kitchen orders
    def __init__(self):
        self.orders = []

    def add_order(self, order, priority):
        # Add orders to the kitchen queue with priority
        self.orders.append((order, priority))
        self.orders.sort(key=lambda x: x[1], reverse=True)  # Higher priority first
        print(f"Order for {order['name']} added to the kitchen queue with priority {priority}")

# Example usage
vip_customer = VIPCustomer(101, "John Smith")
menu_database = MenuDatabase()
kitchen_order_queue = KitchenOrderQueue()

# VIP customer requests a special meal
special_meal = vip_customer.request_special_order("Truffle Pasta", {"truffle": 100, "pasta": 200})

# Add special meal to menu database
menu_database.add_to_menu(special_meal['name'], special_meal)

# Add the meal to the kitchen's priority queue
kitchen_order_queue.add_order(special_meal, priority=10)  # VIP orders might have higher priority


#Use Case 3 (Raise Quality Issue): Pseudo code  
# Classes and functions to handle quality issues for a food importer

class QualityIssue:
    def __init__(self, issue_type, severity, date_created):
        self.issue_type = issue_type
        self.severity = severity
        self.date_created = date_created

class IssueQueue:
    def __init__(self):
        self.issues = []

    def add_issue(self, issue):
        # Add an issue to the queue
        self.issues.append(issue)
        # Sort the issues by severity (higher severity first)
        self.issues.sort(key=lambda x: x.severity, reverse=True)
        print(f"Issue added: {issue.issue_type} with severity {issue.severity} on {issue.date_created}")

    def view_issues(self):
        # View all issues in the queue
        if not self.issues:
            print("No issues currently reported.")
        for issue in self.issues:
            print(f"Issue Type: {issue.issue_type}, Severity: {issue.severity}, Date: {issue.date_created}")

# Example usage
issue_queue = IssueQueue()

# Raising a quality issue
new_issue = QualityIssue("Spoiled Fruit", 9, "2024-04-17")
issue_queue.add_issue(new_issue)

# Another issue
new_issue2 = QualityIssue("Contaminated Vegetables", 8, "2024-04-18")
issue_queue.add_issue(new_issue2)

# Management views the issues
issue_queue.view_issues()


#Use Case 4 (Decide Menu): Pseudo code
# Classes and functions to manage the menu and ingredients databases

class IngredientDatabase:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, ingredient_name, quantity):
        if ingredient_name not in self.ingredients:
            self.ingredients[ingredient_name] = quantity
            print(f"New ingredient added: {ingredient_name}")
        else:
            print(f"Ingredient {ingredient_name} already exists.")

class DishDatabase:
    def __init__(self):
        self.dishes = {}

    def add_dish(self, dish_name, ingredients):
        if dish_name not in self.dishes:
            self.dishes[dish_name] = ingredients
            print(f"New dish added: {dish_name} with ingredients: {ingredients.keys()}")
        else:
            print(f"Dish {dish_name} already exists in the menu.")

class Chef:
    def __init__(self, dish_database, ingredient_database):
        self.dish_database = dish_database
        self.ingredient_database = ingredient_database

    def create_dish(self, dish_name, ingredients):
        # Check if the dish already exists
        if dish_name in self.dish_database.dishes:
            print(f"Dish {dish_name} already exists. No new entry created.")
            return

        # Add the dish to the database
        self.dish_database.add_dish(dish_name, ingredients)

        # Ensure all ingredients are registered in the ingredient database
        for ingredient, quantity in ingredients.items():
            self.ingredient_database.add_ingredient(ingredient, quantity)

# Example usage
ingredient_db = IngredientDatabase()
dish_db = DishDatabase()
chef = Chef(dish_db, ingredient_db)

# Chef decides to add a new dish
chef.create_dish("Quinoa Salad", {"quinoa": 200, "tomatoes": 100, "avocado": 50, "feta cheese": 50})

# Trying to add the same dish again
chef.create_dish("Quinoa Salad", {"quinoa": 200, "tomatoes": 100, "avocado": 50, "feta cheese": 50})
