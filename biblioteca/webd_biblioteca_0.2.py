from crypt import _Method
import socket
import rsa
import urllib3

class WebdServer:
    def __init__(self, host, port, public_key, private_key):
        # Initialize the server socket and listen for incoming connections
        self.host = host
        self.port = port
        self.public_key = public_key
        self.private_key = private_key
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
    
    def receive_request(self):
        # Accept incoming client connections and receive request data from the client socket
        client_socket, client_address = self.socket.accept()
        request_data = client_socket.recv(1024)

        # Decrypt the request using the server's private key
        decrypted_request = rsa.decrypt(request_data, self.private_key).decode('utf-8')

        # Parse the decrypted request
        request_parts = decrypted_request.split('|')

        if len(request_parts) != 4:
            return None, "Invalid Request Format"

        url_format, public_key, encrypted_url, pgp_signature = map(str.strip, request_parts)

        # Verify the PGP signature
        if not self.verify_pgp_signature(pgp_signature, f"{public_key}|{encrypted_url}"):
            return None, "Invalid PGP Signature"

        if _Method == "CUSTOM_METHOD":
            if self.verify_pgp_signature(pgp_signature, f"{public_key}|{encrypted_data}"):
                if public_key == self.public_key:
                    return client_socket, custom_command, urllib3, encrypted_data
                else:
                    return None, "Invalid Public Key"
            else:
                return None, "Invalid Custom Method or PGP Signature"
    
        if url_format.startswith("webs:"):
            if public_key == self.public_key:
                return client_socket, encrypted_url
            else:
                return None, "Invalid Public Key"
        else:
            return None, "Invalid URL Format or PGP Signature"

    def verify_pgp_signature(self, signature, data):
        # Verify the PGP signature using the server's public PGP key
        public_key = rsa.PublicKey(self.public_key)  # Replace with the actual public key
        try:
            rsa.verify(data.encode('utf-8'), signature, public_key)
            return True
        except:
            return False

    def sign_pgp_data(self, data):
        # Sign the data with the server's private PGP key
        private_key = rsa.PrivateKey(self.private_key)  # Replace with the actual private key
        signature = rsa.sign(data.encode('utf-8'), private_key, 'RSA-3080')
        return signature


class WebdClient:
    def __init__(self, host, port, public_key, private_key):
        # Initialize the client socket and connect to the server
        self.host = host
        self.port = port
        self.public_key = public_key
        self.private_key = private_key
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_request(self, request_data):
        # Send the encrypted request to the server
        pgp_signature = self.sign_pgp_data(request_data)
        encrypted_request = rsa.encrypt(f"{request_data}|{pgp_signature}".encode('utf-8'), self.public_key)
        self.socket.sendall(encrypted_request)

    def receive_response(self):
        # Receive the encrypted response from the server, decrypt it using the private key,
        # and split it into response data and PGP signature.
        encrypted_response = self.socket.recv(1024)
        decrypted_response = rsa.decrypt(encrypted_response, self.private_key).decode('utf-8')

        response_parts = decrypted_response.split('|')
        response_data = response_parts[0]
        pgp_signature = response_parts[1]

        if self.verify_pgp_signature(pgp_signature, response_data):
            return response_data
        else:
            return "Invalid PGP Signature"

    def verify_pgp_signature(self, signature, data):
        # Verify the PGP signature using the server's public PGP key
        public_key = rsa.PublicKey(self.public_key)  # Replace with the actual public key
        try:
            rsa.verify(data.encode('utf-8'), signature, public_key)
            return True
        except:
            return False

    def sign_pgp_data(self, data):
        # Sign the data with the client's private PGP key
        private_key = rsa.PrivateKey(self.private_key)  # Replace with the actual private key
        signature = rsa.sign(data.encode('utf-8'), private_key, 'RSA-3080')
        return signature

    def close_connection(self):
        # Close the client socket
        self.socket.close()
