import sqlite3
import json

# Create a file-based SQLite database (persisted to disk)
connection = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the table if it doesn't already exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS vbg_getsupport_ref (
    emailId TEXT,
    parentEmailId TEXT,
    fromAddr TEXT,
    intent TEXT,
    entitiesRequired TEXT,
    entitiesAvailable TEXT
);
'''
cursor.execute(create_table_query)

# Insert dummy data if needed (can be done once or in another file)
dummy_data = [
    ('user1@example.com', 'parent1@example.com', 'from1@example.com', 'support', json.dumps(['entity1', 'entity2']), json.dumps({'available1': 'value1', 'available2': 'value2'})),
    ('user2@example.com', 'parent2@example.com', 'from2@example.com', 'help', json.dumps(['entity3']), json.dumps({'available3': 'value3'})),
]

insert_data_query = '''
INSERT INTO vbg_getsupport_ref (emailId, parentEmailId, fromAddr, intent, entitiesRequired, entitiesAvailable)
VALUES (?, ?, ?, ?, ?, ?);
'''

cursor.executemany(insert_data_query, dummy_data)
connection.commit()

# Close the connection
connection.close()
