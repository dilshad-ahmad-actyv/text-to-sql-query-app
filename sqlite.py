import sqlite3

# Connect sqllite database(if it doesn't exist it will be created)
connection = sqlite3.connect('test.db')

# Create a cursor object to execute the SQL query
cursor = connection.cursor()

# Create a table 

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
    )
'''
)

# insert the data into the table

cursor.execute(
    "INSERT INTO users (name, age) VALUES(?, ?)", ("Ram", 30)
)
cursor.execute(
    "INSERT INTO users (name, age) VALUES(?, ?)", ("Mahesh", 23)
)

# cursor.execute("""""")  
# commit the changes to the database
connection.commit()

# retrieve data from all

cursor.execute("SELECT * FROM users")
data = cursor.fetchall()

for row in data:
    print(row)