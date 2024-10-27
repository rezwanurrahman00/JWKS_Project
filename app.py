from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    token = data.get('token')

    # Validate the JWT (placeholder)
    if not token:  # Add real JWT validation here
        return jsonify({'error': 'Invalid token'}), 401

    # Here you can add your logic to authenticate the token and return a response
    return jsonify({'message': 'Authenticated successfully'}), 200

@app.route('/.well-known/jwks.json', methods=['GET'])
def jwks():
    conn = sqlite3.connect('totally_not_my_privateKeys.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM keys')
    keys = cursor.fetchall()
    conn.close()

    # Construct JWKS response
    jwks_keys = []
    for key in keys:
        jwks_keys.append({
            "alg": "RS256",
            "e": key[2]["e"],
            "kid": key[1],
            "kty": "RSA",
            "n": key[2]["n"],
            "use": "sig"
        })

    return jsonify({'keys': jwks_keys}), 200

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)

