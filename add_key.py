# add_key.py
import sqlite3
import time
import os

def add_key():
    # Check if the database file exists
    db_file = 'totally_not_my_privateKeys.db'
    if not os.path.exists(db_file):
        print("Database file does not exist. Please run the key generation first.")
        return
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Define a real key and expiration time (10 minutes from now)
    private_key = "your_real_private_key"  # Replace with actual key generation logic
    exp_time = int(time.time()) + 600  # 10 minutes from now
    
    # Insert the key and expiration time into the database
    cursor.execute("INSERT INTO keys (key, exp) VALUES (?, ?)", (private_key, exp_time))
    conn.commit()
    conn.close()
    print("Key added successfully.")

if __name__ == "__main__":
    add_key()

