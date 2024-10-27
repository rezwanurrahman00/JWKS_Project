Project 2: JWKS Server with JWT Authentication
Overview
This project involves creating a JSON Web Key Set (JWKS) server that issues JSON Web Tokens (JWTs) and provides a JWKS endpoint for public key retrieval. This setup enables secure, token-based authentication by allowing clients to verify issued JWTs using public keys.
Files Included
1. app.py: The main application code for the JWKS server.
2. totally_not_my_privateKeys.db: SQLite database used for storing RSA private keys with expiration.
3. Project_Documentation.pdf (this document).
Requirements
Python 3.x
Flask
SQLite
pyjwt for JWT handling
cryptography for RSA key management
Project Components
1. Application Endpoints
/auth (POST)
Purpose: Issues a JWT token signed with an RSA private key.
Request Parameters:
- expired (optional): If set to true, it will try to retrieve an expired key for testing purposes.
Response:
A JSON object containing the token field with the issued JWT.
Example Response:
{
"token": "<JWT_TOKEN>"
}
/.well-known/jwks.json (GET)
Purpose: Provides a JSON Web Key Set (JWKS) containing public keys for validating JWTs issued by the /auth endpoint.
Response:
A JSON object containing the keys array, where each entry is an RSA public key formatted as required by JWKS specifications.
Example Response:
{
"keys": [
{"kid": "1","kty": "RSA","use": "sig","alg": "RS256","n": "<MODULUS>","e": "65537"}
]
}
2. Security Measures
To ensure secure handling of JWTs and prevent common security vulnerabilities:

RSA Encryption: JWTs are signed using RSA private keys. The public keys are exposed via the JWKS endpoint to allow clients to verify JWT signatures.
Parameterized SQL Queries: SQL queries for retrieving RSA keys from the database are parameterized to prevent SQL injection attacks.
Token Expiration: JWTs issued by the /auth endpoint include an expiration timestamp to limit the token's validity period, reducing risks in case of token leakage.
How to Run the Project
1. Set Up the Environment:
- Ensure that you have all required dependencies installed.
- Run the following command in your terminal:
pip install flask pyjwt cryptography

2. Start the Server:
- In the terminal, navigate to the project directory.
- Run the app.py file:
python app.py

The server will start on http://127.0.0.1:8080.

3. Testing the Endpoints:

Request a JWT:
curl -X POST http://127.0.0.1:8080/auth

Retrieve the JWKS:
curl http://127.0.0.1:8080/.well-known/jwks.json
Troubleshooting
1. Error: "No appropriate key found"
- This means there is no valid key in the database that meets the specified conditions (expired or not).
- Ensure the database is correctly populated with RSA keys.

2. AttributeError: 'bytes' object has no attribute 'encode'
- This error occurs if there’s an encoding issue with the keys. Ensure that when loading private keys, they are in byte format directly from the database.
Additional Notes
Ensure to close the server and terminate any processes if you're running multiple instances of app.py.
Always test the endpoints after any modification to ensure proper functionality.
