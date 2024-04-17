# DELIVERY DELIVERY DELIVERY  DELIVERY  DELIVERY 
#Use Case 1 (Accept delivery): Pseudo code 
# Classes and functions to manage delivery orders

class Order:
    def __init__(self, order_id, customer, details):
        self.order_id = order_id
        self.customer = customer
        self.details = details
        self.is_delivery = False

class DeliveryQueue:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        # Only add to delivery queue if it is marked as a delivery
        if order.is_delivery:
            self.orders.append(order)
            print(f"Order {order.order_id} added to delivery queue")

    def get_next_order(self):
        # Get the next order from the queue (assuming FIFO for simplicity)
        return self.orders.pop(0) if self.orders else None

class Driver:
    def __init__(self, driver_id, name):
        self.driver_id = driver_id
        self.name = name
        self.current_delivery = None

    def pick_up_order(self, delivery_queue):
        # Driver picks up the next order in the delivery queue
        order = delivery_queue.get_next_order()
        if order:
            self.current_delivery = order
            print(f"Driver {self.name} picked up order {order.order_id}")
        else:
            print(f"No orders to pick up for driver {self.name}")

# Example usage
# Creating a list of orders
orders = [Order(1, 'Customer 1', 'Meal 1'), Order(2, 'Customer 2', 'Meal 2')]
orders[0].is_delivery = True  # Mark the first order as a delivery
orders[1].is_delivery = True  # Mark the second order as a delivery

# Create a delivery queue and add orders to it
delivery_queue = DeliveryQueue()
for order in orders:
    delivery_queue.add_order(order)

# Create a driver and pick up the next order
driver = Driver(101, 'John')
driver.pick_up_order(delivery_queue)



#Use Case 2 (Accept delivery): Pseudo code 
# Define the classes for DeliveryPersonnel, Feedback, and Management

class DeliveryPersonnel:
    def __init__(self, id):
        self.id = id

    def receive_feedback(self, customer_feedback):
        # Delivery personnel receive feedback from the customer
        print(f"Feedback received from customer: {customer_feedback}")
        return customer_feedback

    def report_feedback(self, feedback):
        # Report the feedback using the FeedbackForm
        feedback_form = FeedbackForm()
        feedback_form.submit_feedback(feedback, self.id)

class FeedbackForm:
    def submit_feedback(self, feedback, delivery_personnel_id):
        # Submit feedback to the FeedbackDatabase
        feedback_database.store_feedback(feedback, delivery_personnel_id)

class FeedbackDatabase:
    feedback_list = []

    @classmethod
    def store_feedback(cls, feedback, delivery_personnel_id):
        # Store the feedback in the database
        cls.feedback_list.append({'delivery_personnel_id': delivery_personnel_id, 'feedback': feedback})
        print(f"Feedback stored in database: {feedback}")

class FeedbackProcessingSystem:
    def process_feedback(cls, feedback_list):
        # Process the feedback for categorization and analysis
        for feedback in feedback_list:
            # Placeholder for processing logic
            pass
        # Make processed feedback available for management and delivery personnel
        ManagementDashboard.update_dashboard(feedback_list)
        DeliveryTeamInterface.update_feedback_view(feedback_list)

class ManagementDashboard:
    @staticmethod
    def update_dashboard(feedback_list):
        # Update management dashboard with new feedback
        print("Management dashboard updated with feedback.")

class DeliveryTeamInterface:
    @staticmethod
    def update_feedback_view(feedback_list):
        # Update delivery team's interface with feedback summaries
        print("Delivery team interface updated with feedback summaries.")

# Usage

# Instantiate the classes
delivery_personnel = DeliveryPersonnel(123)
feedback_database = FeedbackDatabase()
feedback_processing_system = FeedbackProcessingSystem()

# Simulate receiving feedback from a customer
feedback = delivery_personnel.receive_feedback("Excellent service!")

# Simulate reporting feedback
delivery_personnel.report_feedback(feedback)

# Assume that feedback processing happens at regular intervals
feedback_processing_system.process_feedback(FeedbackDatabase.feedback_list)


#Use Case 3 (View delivery ratings): Pseudo code 
# A class to represent the ratings database where all customer ratings are stored
class RatingsDatabase:
    ratings = []

    def store_rating(self, rating):
        # Store the integer rating in the database
        self.ratings.append(rating)

    def retrieve_ratings(self):
        # Retrieve all stored ratings
        return self.ratings

# A class to calculate and provide statistics on the ratings
class StatisticsProcessor:
    def calculate_mean(self, ratings):
        # Calculate the mean of the ratings
        return sum(ratings) / len(ratings)

    def calculate_median(self, ratings):
        # Calculate the median of the ratings
        ratings.sort()
        mid = len(ratings) // 2
        return (ratings[mid] + ratings[-mid-1]) / 2 if len(ratings) % 2 == 0 else ratings[mid]

    def calculate_distribution(self, ratings):
        # Calculate the distribution and return a histogram representation
        histogram = {1:0, 2:0, 3:0, 4:0, 5:0}
        for rating in ratings:
            histogram[rating] += 1
        return histogram

# A class for the driver to view their ratings
class Driver:
    def __init__(self, database, statistics_processor):
        self.database = database
        self.statistics_processor = statistics_processor

    def view_ratings(self):
        # Retrieve ratings and display statistics
        ratings = self.database.retrieve_ratings()
        print("Mean Rating:", self.statistics_processor.calculate_mean(ratings))
        print("Median Rating:", self.statistics_processor.calculate_median(ratings))
        print("Ratings Distribution:", self.statistics_processor.calculate_distribution(ratings))

# Example usage:
# Initialize the database and statistics processor
ratings_db = RatingsDatabase()
stats_processor = StatisticsProcessor()

# Simulate storing ratings from customers
ratings_db.store_rating(5)
ratings_db.store_rating(3)
ratings_db.store_rating(4)
ratings_db.store_rating(1)
ratings_db.store_rating(5)

# Driver wants to view their ratings
driver = Driver(ratings_db, stats_processor)
driver.view_ratings()
