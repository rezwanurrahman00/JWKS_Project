from Crypto.PublicKey import RSA
import json
import sqlite3

def generate_rsa_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Save keys to the database
    add_key_to_db("1", {
        "e": key.e,
        "n": key.n,
        "alg": "RS256",
        "kty": "RSA"
    })

    return private_key, public_key

if __name__ == "__main__":
    generate_rsa_key()

