import pyodbc

# Connect and pull data from a SQL Server database.
class Database:

    # Class Attributes for SQL Server database. Note. These variables will change depending on computer and project.
    Driver = '{ODBC Driver 17 for SQL Server}'
    Server = 'DESKTOP-OFNPJHO'
    Database = 'change_Var'
    Trusted_Connection = 'yes'

    # Instance Attributes
    def __init__(self, Driver, Server, Database, Trusted_Connection):
        self.Driver = Driver
        self.Server = Server
        self.Database = Database
        self.Trusted_Connection = Trusted_Connection

    # Properties
    @property
    def EstablishConnection(self):
        return f'''DRIVER={self.Driver};
                   SERVER={self.Server};
                   DATABASE={self.Database};
                   TRUSTED_CONNECTION={self.Trusted_Connection}'''
