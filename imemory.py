import sqlite3
import json

# Step 1: Create an in-memory SQLite database
connection = sqlite3.connect(':memory:')  # This will create a database in memory

# Step 2: Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Step 3: Create the table with the structure similar to your provided image
create_table_query = '''
CREATE TABLE vbg_getsupport_ref (
    emailId TEXT,
    parentEmailId TEXT,
    fromAddr TEXT,
    intent TEXT,
    entitiesRequired TEXT,
    entitiesAvailable TEXT
);
'''
# Execute the query to create the table
cursor.execute(create_table_query)

# Step 4: Insert dummy data into the table
# Prepare the data
insert_data_query = '''
INSERT INTO vbg_getsupport_ref (emailId, parentEmailId, fromAddr, intent, entitiesRequired, entitiesAvailable)
VALUES (?, ?, ?, ?, ?, ?);
'''

# Example dummy data
dummy_data = [
    ('user1@example.com', 'parent1@example.com', 'from1@example.com', 'support', json.dumps(['entity1', 'entity2']), json.dumps({'available1': 'value1', 'available2': 'value2'})),
    ('user2@example.com', 'parent2@example.com', 'from2@example.com', 'help', json.dumps(['entity3']), json.dumps({'available3': 'value3'})),
]

# Insert dummy data
cursor.executemany(insert_data_query, dummy_data)

# Commit the transaction
connection.commit()

# Step 5: Retrieve and display the inserted data
cursor.execute("SELECT * FROM vbg_getsupport_ref")
rows = cursor.fetchall()

# Step 6: Display the results
for row in rows:
    print(row)

# Step 7: Close the connection when done
connection.close()
