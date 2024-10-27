from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sqlite3
import time

# Generate an RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serialize the private key in PEM format
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Connect to the SQLite database
conn = sqlite3.connect('totally_not_my_privateKeys.db')
cursor = conn.cursor()

# Insert the PEM-encoded private key and expiration into the database
exp_time = int(time.time()) + 600  # Expires in 10 minutes
cursor.execute("INSERT INTO keys (key, exp) VALUES (?, ?)", (pem_private_key, exp_time))
conn.commit()
conn.close()

print("RSA private key generated and saved to database.")
