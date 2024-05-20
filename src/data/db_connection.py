import sqlalchemy


# Connect and pull data from a SQL Server database.
class Database:

    # Class Attributes for SQL Server database. Note: These variables will change depending on computer and project.
    # N/A

    # Instance Attributes
    def __init__(self, driver, server, database, trusted_connection):
        self.driver = driver
        self.server = server
        self.database = database
        self.trusted_connection = trusted_connection

    def establish_connection(self):
        connection_string = Database.self() #'{self.driver}/{self.database}?driver={self.driver}&Trusted_Connection={self.trusted_connection}'
        connection_url = sqlalchemy.URL.create(f'mssql+pyodbc://@{self.trusted_connection}@{self.server}/{self.database}?driver={self.driver}')
        print('Successfully connected!!')
        return connection_url

    def create_db_engine(self):
        connection_string = self.establish_connection()
        engine = sqlalchemy.create_engine(connection_string)
        print('Hello')
        return engine 
    
    def hello():
        print('hello')