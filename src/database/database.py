import os
import sqlalchemy
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError as sqlexception


# Connect and pull data from a SQL Server database
class database:

    def __init__(self, driver, server, database, trusted_connection):
        self.driver = driver
        self.server = server
        self.database = database
        self.trusted_connection = trusted_connection

    def connection_url(self):
        '''Example: Database(driver='ODBC+Driver+17+for+SQL+Server',server='DESKTOP-OFNPJHO',database='PakistanUsedCars',trusted_connection='yes')'''
        connection_url = f"mssql+pyodbc://{self.server}/{self.database}?driver={self.driver};Trusted_Connection={self.trusted_connection}"
        return connection_url

    def create_db_engine(self):
        connection_string = self.connection_url()
        try:
            engine = sqlalchemy.create_engine(connection_string)
            return engine 
        except sqlexception as e:
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
        except sqlexception as e:
            print(f"Error loading query: {e}")
            return None

    def execute_query(self, query_file):        
        '''Note: Instantiate object, give sql file path, then call this method (e.g. - db.execute_query(query_file))'''
        engine = self.create_db_engine()
        query = self.load_query(query_file)
        try: 
            with engine.connect() as connection:
                result = connection.execute(sqlalchemy.text(query))
                df = pd.DataFrame(result.fetchall(), columns=result.keys())
            return df
        except sqlexception as e:
            print(f"Error executing query: {e}")
            return None 
        
    def save_to_csv(self, df, output_file_folder, csv_name):
        '''Note: use rf'' when defining the absolute query path'''
        '''Run this method after execute_query()'''
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_file_path = os.path.join(output_file_folder, csv_name)
        csv_file_path = os.path.join(current_dir, 'csv', output_file_path)
        try:
            df.to_csv(csv_file_path, index=False)
        except PermissionError as e:
            print(f"Permission denied: {e}")
        except FileNotFoundError as e:
            print(f"File not found: {e}")
