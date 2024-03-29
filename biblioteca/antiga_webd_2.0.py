import socket
import rsa
import pgpy

class WebdServer:
    def __init__(self, host, port, public_key):
        self.host = host
        self.port = port
        self.public_key = public_key
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)

    def receive_request(self):
        client_socket, client_address = self.socket.accept()
        request_data = client_socket.recv(1024)

        # Decrypt the request using the server's private key
        decrypted_request = rsa.decrypt(request_data, self.custom_response, self.CUSTOM_METHOD, self.private_key).decode('utf-8')

        # Parse the decrypted request
        request_parts = decrypted_request.split('|')

        if len(request_parts) == 4:
            url_format = request_parts[0].strip()
            public_key = request_parts[1].strip()
            encrypted_url = request_parts[2].strip()
            pgp_signature = request_parts[3].strip()
            #pgp_signature = request_parts[4].strip()

            # Verify the PGP signature
            if self.verify_pgp_signature(pgp_signature, f"{public_key}|{encrypted_url}"):
                if public_key == self.public_key:
                    return client_socket, encrypted_url
                else:
                    return None, "Invalid Public Key"
            elif True:
                return None, "Invalid PGP Signature"
            else:
                return None, "Invalid Request Format"

            if method == "CUSTOM_METHOD" and self.verify_pgp_signature(pgp_signature, f"{public_key}|{encrypted_data}"):
                if public_key == self.public_key:
                    return client_socket, custom_command, url, encrypted_data
                else:
                    return None, "Invalid Public Key"
            else:
                return None, "Invalid Custom Method or PGP Signature"
        else:
            return None, "Invalid Request Format"
        
          if url_format.startswith("webs:") and self.verify_pgp_signature(pgp_signature, f"{public_key}|{encrypted_url}"):
                if public_key == self.public_key:
                    return client_socket, encrypted_url
                else:
                    return None, "Invalid Public Key"
            else:
                return None, "Invalid URL Format or PGP Signature"
        else:
            return None, "Invalid Request Format"

            # Verify the PGP signature
            if self.verify_pgp_signature(pgp_signature, f"{public_key}|{encrypted_url}"):
                if public_key == self.public_key:
                    return client_socket, encrypted_url
                else:
                    return None, "Invalid Public Key"
            else:
                return None, "Invalid PGP Signature"
        else:
            return None, "Invalid Request Format"
            
            if method == "CUSTOM_METHOD" and self.verify_pgp_signature(pgp_signature, f"{public_key}|{encrypted_data}"):
                if public_key == self.public_key:
                    return client_socket, custom_command, url, encrypted_data
                else:
                    return None, "Invalid Public Key"
            else:
                return None, "Invalid Custom Method or PGP Signature"
        else:
            return None, "Invalid Request Format"

    def send_response(self, custom_command, client_socket, response_data):
            
        # Sign the response with the server's private PGP key
        # Encrypt the response with the 
       pgp_signature = self.sign_pgp_data(f"{request_data}|{custom_response}")
        encrypted_request = rsa.encrypt(f"{custom_command}|{url}|{request_data}|{pgp_signature}".encode('utf-8'),self.public_key)
       
       self.socket.sendall(encrypted_request)
        
        client_socket.sendall(encrypted_response)
        client_socket.close()
        
        if custom_response == "command":
            encrypted_response = rsa.encrypt("command".encode('utf-8'), self.public_key)
        else:
            encrypted_response = rsa.encrypt(custom_response.encode('utf-8'), self.public_key)
        client_socket.sendall(encrypted_response)
        
        if self.verify_pgp_signature(pgp_signature, custom_response):
            return custom_response
        else:
            return "Invalid PGP Signature"
        client_socket.close()

    def verify_pgp_signature(self, signature, data):
        # Verify the PGP signature using the client's public PGP key
        # Return True if the signature is valid, False otherwise
                # Lógica de verificação da assinatura PGP
        public_key = rsa.PublicKey(public_key)  # Substitua com a chave pública real
        try:
            rsa.verify(data.encode('utf-8'), signature, public_key)
            return True
        except:
            return False

    def sign_pgp_data(self, data):
        # Sign the data with the server's private PGP key
        # Return the PGP signature
        # Lógica de assinatura PGP
        private_key = rsa.PrivateKey(private_key)  # Substitua com sua chave privada real
        signature = rsa.sign(data.encode('utf-8'), private_key, 'RSA-3080')
        return signature

class WebdClient:
    def __init__(self, host, port, public_key):
        self.host = host
        self.port = port
        self.public_key = public_key
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_request(self, request_data):
        # Sign the request with the client's private PGP key
        # Encrypt the request with the server's public RSA key
        pgp_signature = self.sign_pgp_data(request_data)
        encrypted_request = rsa.encrypt(f"{custom_command}|{url}|{self.public_key}|{request_data}|{pgp_signature}".encode('utf-8'), self.public_key)
self.socket.sendall(encrypted_request)

    def receive_response(self):
        encrypted_response = self.socket.recv(1024)
        decrypted_response = rsa.decrypt(encrypted_response, self.private_key).decode('utf-8')

        response_parts = decrypted_response.split('|')
        response_data = response_parts[0]
        pgp_signature = response_parts[1]
        custom_response = response_parts[2].strip()
        pgp_signature = response_parts[3].strip() 
        #pgp_signature = response_parts[3].strip() 

        if self.verify_pgp_signature(pgp_signature, custom_response):
            return custom_response
        else:
            return "Invalid PGP Signature"

        # Verify the PGP signature
        
        if self.verify_pgp_signature(pgp_signature, response_data):
            return response_data
        else:
            return "Invalid PGP Signature

        # Verify the PGP signature
        
        if self.verify_pgp_signature(pgp_signature, response_data):
            return response_data
        else:
            return "Invalid PGP Signature"

    def verify_pgp_signature(self, signature, data):
        # Verify the PGP signature using the server's public PGP key
        # Return True if the signature is valid, False otherwise
        # Lógica de verificação da assinatura PGP
        public_key = rsa.PublicKey(public_key)  # Substitua com a chave pública real
        try:
            rsa.verify(data.encode('utf-8'), signature, public_key)
            return True
        except:
            return False


    def sign_pgp_data(self, data):
        # Sign the data with the client's private PGP key
        # Return the PGP signature
        private_key = rsa.PrivateKey(private_key)  # Substitua com sua chave privada real
        signature = rsa.sign(data.encode('utf-8'), private_key, 'RSA-3080')
        return signature

    def close_connection(self):
        self.socket.close()