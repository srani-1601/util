import sqlite3

# Connect to the same file-based SQLite database
connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

# Retrieve the data from the table
cursor.execute("SELECT * FROM vbg_getsupport_ref")
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the connection
connection.close()
