import sqlite3

# Connect to the database (it will create the file if it doesn't exist)
conn = sqlite3.connect('outline_keys.db')
cursor = conn.cursor()

# Create a table for storing IPs and outline keys
cursor.execute('''
CREATE TABLE IF NOT EXISTS outline_keys (
    id INTEGER PRIMARY KEY,
    ip TEXT UNIQUE,
    outline_key TEXT
)
''')

# Save changes and close the connection
conn.commit()
conn.close()
print("Database and table created successfully.")

