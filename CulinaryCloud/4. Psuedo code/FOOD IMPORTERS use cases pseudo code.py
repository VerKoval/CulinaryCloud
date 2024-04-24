#FOOD IMPORTERS    FOOD IMPORTERS    FOOD IMPORTERS     FOOD IMPORTERS 
#Use Case 1 (Manage Inventory): Pseudo code 
# Class to manage the inventory of ingredients
// Main Program
Start Program
    While program is running:
        If new shipment arrives:
            UpdateInventory()
    End While
End Program

// Function to update the inventory database with new shipments
Function UpdateInventory
    ingredientDetails = GetNewShipmentDetails()
    For each ingredient in ingredientDetails:
        If IngredientExistsInDatabase(ingredient.name):
            UpdateExistingIngredient(ingredient)
        Else:
            AddNewIngredient(ingredient)
    Display message "Inventory updated successfully."

// Function to get details of new shipment from the food importer
Function GetNewShipmentDetails
    details = []
    count = Input "Enter the number of different ingredients in the shipment:"
    For i from 1 to count:
        name = Input "Enter ingredient name:"
        type = Input "Enter ingredient type (dairy, meat, vegetable, etc.):"
        shipmentDate = Input "Enter date of shipment (YYYY-MM-DD):"
        expirationDate = Input "Enter date of expiration (YYYY-MM-DD):"
        quantity = Input "Enter quantity:"
        details.append({
            "name": name,
            "type": type,
            "shipmentDate": shipmentDate,
            "expirationDate": expirationDate,
            "quantity": quantity
        })
    Return details

// Function to check if ingredient already exists in the database
Function IngredientExistsInDatabase(name)
    Connect to Database
    Search for ingredient by name
    If ingredient found:
        Return true
    Return false

// Function to update existing ingredient in the database
Function UpdateExistingIngredient(ingredient)
    Connect to Database
    Update ingredient entry with new shipment date, expiration date, and adjust quantity
    Close Database Connection

// Function to add new ingredient to the database
Function AddNewIngredient(ingredient)
    Connect to Database
    Insert new ingredient into the database with all attributes
    Close Database Connection



#Use Case 2 (Raise Quality Issue): Pseudo code (mimics chefs raise quality issue code)
# Classes and functions to handle quality issues specifically for food importers
// Main Program
Start Program
    While program is running:
        If quality issue reported:
            ReportQualityIssue()
    End While
End Program

// Function to report a quality issue
Function ReportQualityIssue
    issueDetails = GetQualityIssueDetails()
    AddIssueToQueue(issueDetails)
    Display message "Quality issue reported successfully."

// Function to get details of the quality issue
Function GetQualityIssueDetails
    type = Input "Enter the type of issue (e.g., spoilage, contamination):"
    severity = Input "Choose severity level (1=Low, 5=High):"
    description = Input "Enter a brief description of the issue:"
    dateCreated = GetCurrentDate()
    return {
        "type": type,
        "severity": severity,
        "description": description,
        "dateCreated": dateCreated
    }

// Function to add the quality issue to a queue
Function AddIssueToQueue(issue)
    Connect to Database
    Insert issue into quality issues table with attributes (type, severity, description, dateCreated)
    Close Database Connection

// Utility function to get the current date
Function GetCurrentDate
    // This function retrieves the current system date
    Return system.currentDate()
