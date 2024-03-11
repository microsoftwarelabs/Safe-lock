import socket
import rsa
import pgpy
from pgpy import PGPMessage, PGPKey
from pgpy.constants import PubKeyAlgorithm
from pgpy.errors import PGPError



class CustomHTTPServer:
    def self. __init__(self, host, port, public_key, pgp_public_key):
        self.host = host
        self.port = port
        self.public_key = public_key
        self.pgp_public_key = pgp_public_key
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
                if pgp_public_key == self.pgp_public_key:
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

    def verify_pgp_signature(self, signature, data, public_key):
        try:
        # Verify the PGP signature using the client's public PGP key
        # Return True if the signature is valid, False otherwise
                # Lógica de verificação da assinatura PGP
        #from_blob(data) 
        public_key = pgp_public_key_client
        signature = pgp_public_key_client
        data = data
         
        
        punlic_key.verify(data, signature)
                print("A assinatura PGP é válida.") 
                except pgpy.errors.PGPError: 
                    print("assinatura PGP invalida")

    def sign_pgp_data(self, data,private_key_passphrase, private_key):
        # Sign the data with the server's private PGP key
        # Return the PGP signature
        # Lógica de assinatura PGP
    try:
        # Carregar a chave privada
        key, _ = PGPKey.from_blob(private_key)
        key.unlock(private_key_passphrase)

        # Criar a mensagem com os dados
        message = PGPMessage.new(data, sensitive=True)

        # Assinar a mensagem
        signature = signed_message
        signed_message = key.sign(message)

        # Retornar a assinatura PGP
        return signature
    except PGPError as e:
        print("Erro ao criar a assinatura PGP:", e)

class CustomHTTPClient:
    def __init__(self, host, port, public_key, pgp_public_key):
        self.host = host
        self.port = port
        self.public_key = public_key
        self.pgp_public_key_client = pgp_public_key_client
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

        if self.verify_pgp_signature(pgp_signature, custom_response, custom_response, data, response_data):
            return custom_response
        else:
            return "Invalid PGP Signature"

    def verify_pgp_signature(self, signature, data, public_key):
        # Verify the PGP signature using the server's public PGP key
        # Return True if the signature is valid, False otherwise
        # Lógica de verificação da assinatura 
        try: 
            
        message = PGPMessage.from_blob(data) 
        
        # Carregar a chave pública 
        key, _ = PGPKey.from_blob(public_key) 
        verified = message.verify(key) if 
        
        verified: 
            print("A assinatura PGP é válida.") 
            else: 
                print("A assinatura PGP é inválida.") 
                except PGPError as e: 
                    print("Erro ao verificar a assinatura PGP:", e) 

    def sign_pgp_data(self, data, private_key_passphrase, private_key):
        # Sign the data with the client's private PGP key
        # Return the PGP signature
    try:
        # Carregar a chave privada
        key, _ = PGPKey.from_blob(private_key)
        key.unlock(private_key_passphrase)

        # Criar a mensagem com os dados
        message = PGPMessage.new(data, sensitive=True)

        # Assinar a mensagem
        signature = signat
        signat = key.sign(message)

        # Retornar a assinatura PGP
        return signature
    except PGPError as e:
        print("Erro ao criar a assinatura PGP:", e)

        
    def close_connection(self):
        self.socket.close()
