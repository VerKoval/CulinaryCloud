from Chef import Chef
import Database

chef1 = Chef(1001, 'John Smith', 50000)
chef2 = Chef(1002, 'Rosalyn Franklin', 50000)

chef1.raiseQualityIssue(2001,'Carrots were not of good quality')
chef1.raiseQualityIssue(2001,'Beans were not of good quality')

# Deletes database at the end (to refresh everything)
Database.delete_database(Database.create_server_connection("localhost", "root", 'CSC322Wei', 'CulinaryCloud'),'CulinaryCloud')