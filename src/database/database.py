import os
import sqlalchemy
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError as exception


# Connect and pull data from a SQL Server database.
class database:

    def __init__(self, driver, server, database, trusted_connection):
        self.driver = driver
        self.server = server
        self.database = database
        self.trusted_connection = trusted_connection

    def connection_url(self):
        '''Note: Driver must have '+' between words'''
        '''Example: Database(driver='ODBC+Driver+17+for+SQL+Server',server='DESKTOP-OFNPJHO',database='PakistanUsedCars',trusted_connection='yes')'''
        connection_url = f"mssql+pyodbc://{self.server}/{self.database}?driver={self.driver};Trusted_Connection={self.trusted_connection}"
        return connection_url

    def create_db_engine(self):
        connection_string = self.connection_url()
        try:
            engine = sqlalchemy.create_engine(connection_string)
            return engine 
        except exception as e:
            print(f"Error creating database engine: {e}")
            return None
        
    def load_query(self, query_file):
        '''Note: use rf'' when defining the absolute query path'''
        current_dir = os.path.dirname(os.path.abspath(__file__))
        query_file = os.path.join(current_dir, 'sql', query_file)
        try:
            with open(query_file, 'r') as file:
                query = file.read()
            return query
        except exception as e:
            print(f"Error loading query: {e}")
            return None

    def execute_query(self, query_file):        
        engine = self.create_db_engine()
        query = self.load_query(query_file)
        try: 
            with engine.connect() as connection:
                result = connection.execute(sqlalchemy.text(query))
                df = pd.DataFrame(result.fetchall(), columns=result.keys())
            return df
        except exception as e:
            print(f"Error executing query: {e}")
            return None 
