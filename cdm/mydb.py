import mysql.connector

data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Root.123'
)

# prepare cursor object
cursor_object = data_base.cursor()

# create a database
cursor_object.execute("CREATE DATABASE customer_database")

print("Done")