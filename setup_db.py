# setup_db.py
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('totally_not_my_privateKeys.db')
cursor = conn.cursor()

# Create the keys table
cursor.execute('''
CREATE TABLE IF NOT EXISTS keys (
    kid INTEGER PRIMARY KEY AUTOINCREMENT,
    key BLOB NOT NULL,
    exp INTEGER NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table 'keys' created successfully.")
