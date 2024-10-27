import sqlite3

def setup_database():
    conn = sqlite3.connect('totally_not_my_privateKeys.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS keys (
            id INTEGER PRIMARY KEY,
            key_id TEXT NOT NULL,
            key TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()

