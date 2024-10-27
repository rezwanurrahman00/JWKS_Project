# add_key.py
import sqlite3
import time

def add_key():
    # Connect to the SQLite database
    conn = sqlite3.connect('totally_not_my_privateKeys.db')
    cursor = conn.cursor()
    
    # Define a sample key and expiration time (10 minutes from now)
    private_key = "sample_private_key"
    exp_time = int(time.time()) + 600  # 10 minutes from now
    
    # Insert the key and expiration time into the database
    cursor.execute("INSERT INTO keys (key, exp) VALUES (?, ?)", (private_key, exp_time))
    conn.commit()
    conn.close()
    print("Key added successfully.")

if __name__ == "__main__":
    add_key()
