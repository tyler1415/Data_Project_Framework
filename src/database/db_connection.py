import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError as exception


# Connect and pull data from a SQL Server database.
class Database_Connection:

    # Class Attributes for SQL Server database. Note: These variables will change depending on computer and project.
    # N/A

    # Instance Attributes
    def __init__(self, driver, server, database, trusted_connection):
        self.driver = driver
        self.server = server
        self.database = database
        self.trusted_connection = trusted_connection

    def establish_connection(self):
        connection_url = f"mssql+pyodbc://{self.server}/{self.database}?driver={self.driver};Trusted_Connection={self.trusted_connection}"
        return connection_url

    def create_db_engine(self):
        connection_string = self.establish_connection()
        engine = sqlalchemy.create_engine(connection_string)
        return engine 

    def connect(self):
        try:
            connection = self.create_db_engine().connect()
            print('Database connection established.')
            return connection
        except exception as e:
            print(f"Error connecting to database: {e}")
            return None
        
    def close(self, connection):
        try:
            connection.close()
            print('Database connection closed.')
        except exception as e:
            print(f"Error closing connection: {e}")
