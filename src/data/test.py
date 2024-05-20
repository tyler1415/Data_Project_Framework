from db_connection import *


dbConn = Database('{ODBC+Driver+17+for+SQL+Server}','DESKTOP-OFNPJHO', 'PakistanUsedCars','yes')

print(Database.establish_connection(dbConn))

#Database.hello()

