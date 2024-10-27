import sqlite3
import json

def add_key_to_db(key_id, key):
    # Connect to the SQLite database
    conn = sqlite3.connect('totally_not_my_privateKeys.db')
    cursor = conn.cursor()

    # Ensure the keys table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS keys (
            id INTEGER PRIMARY KEY,
            key_id TEXT NOT NULL,
            key TEXT NOT NULL
        )
    ''')

    # Insert the new key into the database
    cursor.execute('''
        INSERT INTO keys (key_id, key) VALUES (?, ?)
    ''', (key_id, json.dumps(key)))  # Store key as JSON string

    conn.commit()
    conn.close()

# Example usage:
if __name__ == "__main__":
    key_id = "1"  # Replace with your key id logic
    key = {
        "alg": "RS256",
        "e": "65537",
        "kid": key_id,
        "kty": "RSA",
        "n": "your_modulus_here",  # Use your modulus value
        "use": "sig"
    }
    add_key_to_db(key_id, key)


