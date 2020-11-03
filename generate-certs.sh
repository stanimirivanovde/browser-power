# Generate a certificate and a key with no password and setup the CN and Subject Alternate Name so Chrome
# doesn't complain that it is not set.
/usr/local/opt/openssl/bin/openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes \
    -new -subj "/C=GB/CN=192.168.93.122" \
    -addext "subjectAltName = DNS:localhost" \
    -addext "certificatePolicies = 1.2.3.4"
