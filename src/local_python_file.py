from database.database import Database

db = Database(driver='ODBC+Driver+17+for+SQL+Server',server='DESKTOP-OFNPJHO',database='PakistanUsedCars',trusted_connection='yes')
query_file = rf"C:\Users\tgmce\OneDrive\Desktop\Data_Project_Framework\src\resources\sql\query_1.sql"
result = db.execute_query(query_file)