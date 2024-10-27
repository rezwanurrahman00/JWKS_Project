from flask import Flask, jsonify, request
import sqlite3
import time
import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('totally_not_my_privateKeys.db')

def get_key_from_db(expired=False):
    conn = connect_db()
    cursor = conn.cursor()
    current_time = int(time.time())
    if expired:
        cursor.execute("SELECT key FROM keys WHERE exp <= ?", (current_time,))
    else:
        cursor.execute("SELECT key FROM keys WHERE exp > ?", (current_time,))
    key = cursor.fetchone()
    conn.close()
    return key[0] if key else None

@app.route('/auth', methods=['POST'])
def auth():
    expired = request.args.get('expired', 'false').lower() == 'true'
    private_key = get_key_from_db(expired=expired)
    if not private_key:
        return jsonify({"error": "No appropriate key found"}), 404

    # Load private key from the database
    private_key_obj = serialization.load_pem_private_key(
        private_key,
        password=None,
        backend=default_backend()
    )

    payload = {"user": "testuser", "exp": int(time.time()) + 600}  # JWT valid for 10 minutes
    token = jwt.encode(payload, private_key_obj, algorithm='RS256')
    return jsonify({"token": token})

@app.route('/.well-known/jwks.json', methods=['GET'])
def get_jwks():
    conn = connect_db()
    cursor = conn.cursor()
    current_time = int(time.time())
    cursor.execute("SELECT key FROM keys WHERE exp > ?", (current_time,))
    keys = cursor.fetchall()
    conn.close()

    jwks = []
    for i, (key,) in enumerate(keys):
        # Convert the private key to a public key and then serialize it to JSON Web Key (JWK) format
        public_key_obj = serialization.load_pem_private_key(
            key,
            password=None,
            backend=default_backend()
        ).public_key()
        
        public_numbers = public_key_obj.public_numbers()
        jwks.append({
            "kid": str(i + 1),
            "kty": "RSA",
            "use": "sig",
            "n": public_numbers.n,
            "e": public_numbers.e,
            "alg": "RS256"
        })

    return jsonify({"keys": jwks})

if __name__ == '__main__':
    app.run(port=8080, debug=True)
