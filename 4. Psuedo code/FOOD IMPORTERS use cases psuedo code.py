#FOOD IMPORTERS    FOOD IMPORTERS    FOOD IMPORTERS     FOOD IMPORTERS 
#Use Case 1 (Manage Inventory): Pseudo code 
# Class to manage the inventory of ingredients

class Ingredient:
    def __init__(self, name, type, shipment_date, expiration_date, count):
        self.name = name
        self.type = type
        self.shipment_date = shipment_date
        self.expiration_date = expiration_date
        self.count = count

class InventoryDatabase:
    def __init__(self):
        self.ingredients = {}  # Dictionary to store ingredient objects by name

    def add_or_update_ingredient(self, ingredient):
        # Adds a new ingredient to the database or updates existing entry
        if ingredient.name in self.ingredients:
            # Update existing ingredient count and dates
            self.ingredients[ingredient.name].count += ingredient.count
            self.ingredients[ingredient.name].shipment_date = ingredient.shipment_date
            self.ingredients[ingredient.name].expiration_date = ingredient.expiration_date
            print(f"Updated {ingredient.name}: New count is {self.ingredients[ingredient.name].count}")
        else:
            # Add new ingredient
            self.ingredients[ingredient.name] = ingredient
            print(f"Added new ingredient {ingredient.name} to inventory")

    def get_inventory(self):
        # Returns a list of all ingredients in the inventory
        return [(ing.name, ing.count, ing.expiration_date) for ing in self.ingredients.values()]

# Example usage
inventory_db = InventoryDatabase()

# New shipment arrives
new_ingredients = [
    Ingredient("Milk", "Dairy", "2024-04-20", "2024-05-20", 100),
    Ingredient("Beef", "Meat", "2024-04-18", "2024-05-15", 50)
]

# Update inventory with new shipment
for ing in new_ingredients:
    inventory_db.add_or_update_ingredient(ing)

# Display current inventory
current_inventory = inventory_db.get_inventory()
for item in current_inventory:
    print(f"Ingredient: {item[0]}, Count: {item[1]}, Expires: {item[2]}")


#Use Case 2 (Raise Quality Issue): Pseudo code (mimics chefs raise quality issue code)
# Classes and functions to handle quality issues specifically for food importers

class QualityIssue:
    def __init__(self, issue_type, severity, date_created, details):
        self.issue_type = issue_type
        self.severity = severity
        self.date_created = date_created
        self.details = details  # Additional details about the issue

class IssueQueue:
    def __init__(self):
        self.issues = []

    def add_issue(self, issue):
        # Add an issue to the queue
        self.issues.append(issue)
        # Sort the issues by severity (higher severity first)
        self.issues.sort(key=lambda x: x.severity, reverse=True)
        print(f"Issue added: {issue.issue_type} with severity {issue.severity} on {issue.date_created}, details: {issue.details}")

    def view_issues(self):
        # View all issues in the queue
        if not self.issues:
            print("No issues currently reported.")
        for issue in self.issues:
            print(f"Issue Type: {issue.issue_type}, Severity: {issue.severity}, Date: {issue.date_created}, Details: {issue.details}")

# Example usage for a food importer
issue_queue = IssueQueue()

# Raising a quality issue related to a shipment
new_issue = QualityIssue("Contaminated Fruit", 9, "2024-04-17", "Fruit shipment from batch #34 found to be contaminated")
issue_queue.add_issue(new_issue)

# Another issue related to packaging
new_issue2 = QualityIssue("Damaged Packaging", 7, "2024-04-18", "Packaging for seafood shipment compromised")
issue_queue.add_issue(new_issue2)

# Viewing the issues
issue_queue.view_issues()
