#MANAGER  MANAGER   MANAGER   MANAGER   MANAGER    MANAGER   

#Use Case 1 (Manage staff): Pseudo code 
 # Class definitions and functions to handle a restaurant's staff management system
// Main Program
Start Program
    Display Manager Menu:
        1. Promote Staff
        2. Demote Staff
        3. Hire Staff
        4. Fire Staff
    Choose option:
        If option 1:
            PromoteStaff()
        If option 2:
            DemoteStaff()
        If option 3:
            HireStaff()
        If option 4:
            FireStaff()
End Program

// Function to promote staff
Function PromoteStaff
    employeeID = Input "Enter Employee ID:"
    employee = FetchEmployeeFromDatabase(employeeID)
    If employee is not found:
        Display "Employee not found."
        Return
    If employee.numberOfCompliments >= 2:
        UpdateEmployeeTier(employeeID, 1) // Increment tier
        ResetCompliments(employeeID)
        Display "Employee promoted."
    Else:
        Display "Not enough compliments to promote."

// Function to demote staff
Function DemoteStaff
    employeeID = Input "Enter Employee ID:"
    employee = FetchEmployeeFromDatabase(employeeID)
    If employee is not found:
        Display "Employee not found."
        Return
    UpdateEmployeeTier(employeeID, -1) // Decrement tier
    If employee.tier == 0:
        FireStaff(employeeID)
    Display "Employee demoted."

// Function to hire staff
Function HireStaff
    name = Input "Enter name:"
    position = Input "Enter position/role:"
    pay = Input "Enter pay:"
    employeeID = GenerateUniqueEmployeeID()
    AddEmployeeToDatabase(employeeID, name, position, pay)
    Display "New employee hired with ID: " + employeeID

// Function to fire staff
Function FireStaff
    employeeID = Input "Enter Employee ID:"
    RemoveEmployeeFromDatabase(employeeID)
    Display "Employee fired."

// Helper functions for database operations
Function FetchEmployeeFromDatabase(employeeID)
    // Fetch employee details based on Employee ID
    Return employeeDetails or null if not found

Function UpdateEmployeeTier(employeeID, change)
    // Increment or decrement the employee's tier in the database
    // If tier becomes 0, possibly trigger FireStaff()

Function ResetCompliments(employeeID)
    // Set the number of compliments to 0 in the database

Function AddEmployeeToDatabase(employeeID, name, position, pay)
    // Add a new employee entry to the database

Function RemoveEmployeeFromDatabase(employeeID)
    // Remove an employee entry from the database

Function GenerateUniqueEmployeeID
    // Generate a unique ID for a new employee
    Return uniqueID


#Use Case 2 (Handles review): Pseudo code  
# Classes and functions to manage customer reviews
// Main Program
Start Program
    While program is running:
        Display Manager Menu:
            1. View Reviews
            2. Remove Review
        Choose option:
            If option 1:
                ViewReviews()
            If option 2:
                RemoveReview()
End Program

// Function to view reviews
Function ViewReviews
    reviews = FetchAllReviews()
    For each review in reviews:
        Display "Review ID: " + review.id + ", Content: " + review.content + ", Type: " + review.type

// Function to remove a review
Function RemoveReview
    reviewID = Input "Enter Review ID to remove:"
    review = FetchReviewByID(reviewID)
    If review is not found:
        Display "Review not found."
        Return
    RemoveReviewFromDatabase(reviewID)
    IssueWarningToCustomer(review.customerID)
    Display "Review removed and warning issued to the customer."

// Helper functions for database operations
Function FetchAllReviews
    Connect to Database
    Fetch and return all reviews
    Close Database Connection

Function FetchReviewByID(reviewID)
    Connect to Database
    Search for review by ID
    Return review details or null if not found
    Close Database Connection

Function RemoveReviewFromDatabase(reviewID)
    Connect to Database
    Delete review from the reviews table based on ID
    Close Database Connection

Function IssueWarningToCustomer(customerID)
    // Logic to send a warning to the customer based on their review
    SendWarning "Your review has been flagged and removed due to inappropriate content."



#Use Case 3 (Issue warning to customers): Pseudo code 
# Classes and functions to manage customer data and issue warnings
// Main Program
Start Program
    While program is running:
        Display Menu:
            1. Issue Warning to Customer
        Choose option:
            If option 1:
                IssueCustomerWarning()
End Program

// Function to issue a warning to a customer
Function IssueCustomerWarning
    customerID = Input "Enter Customer ID:"
    customer = FetchCustomerByID(customerID)
    If customer is not found:
        Display "Customer not found."
        Return
    IncrementWarningCount(customerID)
    NotifyCustomer(customerID)
    Display "Warning issued to customer ID: " + customerID

// Helper functions for database operations
Function FetchCustomerByID(customerID)
    Connect to Database
    Search for customer by ID
    If customer found:
        Return customer details
    Return null
    Close Database Connection

Function IncrementWarningCount(customerID)
    Connect to Database
    Fetch current warning count for the customer
    Increment the warning count by 1
    Update the customer record with the new warning count
    Close Database Connection

Function NotifyCustomer(customerID)
    // Logic to notify the customer about the warning
    SendNotification "A warning has been added to your profile due to recent activities."



#Use Case 4 (Demote/deregister customer): Pseudo code
# Classes and functions to manage customer data, issue warnings, and handle demotions or deregistrations
// Main Program
Start Program
    While program is running:
        Display Menu:
            1. Evaluate Customer Status
        Choose option:
            If option 1:
                EvaluateCustomerStatus()
End Program

// Function to evaluate and update customer status based on warnings
Function EvaluateCustomerStatus
    customerID = Input "Enter Customer ID:"
    customer = FetchCustomerByID(customerID)
    If customer is not found:
        Display "Customer not found."
        Return

    warningThreshold = 3  // Set warning threshold, e.g., 3 warnings
    If customer.warnings >= warningThreshold:
        If customer.isVIP:
            DemoteCustomer(customerID)
        Else:
            DeregisterCustomer(customerID)
        ClearWarnings(customerID)
        Display "Customer status has been updated."
    Else:
        Display "Customer does not meet criteria for demotion or deregistration."

// Helper functions for database operations
Function FetchCustomerByID(customerID)
    Connect to Database
    Search for customer by ID
    If customer found:
        Return customer details
    Return null
    Close Database Connection

Function DemoteCustomer(customerID)
    Connect to Database
    Update customer to change 'isVIP' attribute from true to false
    Close Database Connection

Function DeregisterCustomer(customerID)
    Connect to Database
    Delete customer record from the database
    Close Database Connection

Function ClearWarnings(customerID)
    Connect to Database
    Reset the warning count for the customer to 0
    Close Database Connection


