# Make sure to use a password, otherwise it will fail
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365