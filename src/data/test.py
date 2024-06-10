from db_connection import Database_Connection
import sqlalchemy

db = Database_Connection(driver='ODBC+Driver+17+for+SQL+Server',server='DESKTOP-OFNPJHO',database='PakistanUsedCars',trusted_connection='yes')
engine = db.create_db_engine()

# Test the connection by executing a simple query
with engine.connect() as connection:
    result = connection.execute(sqlalchemy.text("SELECT count(*) FROM UsedCarsFinal"))
    for row in result:
        print(row)
