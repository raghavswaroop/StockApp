import pyodbc as odbc

# Connection parameters
server = 'spdemo.cqzuwvyrnjqq.eu-north-1.rds.amazonaws.com,1433'
# database = 'master'
username = 'swaroop'
password = 'swaroop123'

# Establish connection
# connection_string = f'DRIVER={{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.0.so.1.1}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};UID={username};PWD={password}'
conn = odbc.connect(connection_string)


conn.close()


    