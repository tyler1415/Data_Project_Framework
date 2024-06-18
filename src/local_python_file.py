from database.database import database
from data_analysis.exploratory_data_analysis import exploratory_data_analysis


db = database(driver='ODBC+Driver+17+for+SQL+Server',server='DESKTOP-OFNPJHO',database='PakistanUsedCars',trusted_connection='yes')
query_file = rf"C:\Users\tgmce\OneDrive\Desktop\Data_Project_Framework\src\resources\sql\query_1.sql"
result = db.execute_query(query_file)

print(result)

eda = exploratory_data_analysis(result)
eda.correlation_matrix()
#output_folder = rf"C:\Users\tgmce\OneDrive\Desktop\Data_Project_Framework\src\resources\csv\raw_csv_files"
#output_file = 'test_1.csv'
#db.save_to_csv(result, output_folder, output_file)



