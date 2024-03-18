import socket
import rsa
import pgpy
from pgpy import PGPMessage, PGPKey
from pgpy.constants import PubKeyAlgorithm
from pgpy.errors import PGPError


class WEBDServer     
    def__init__(self, host, port, rsa_public_key_serve, pgp_public_key_serve):
        self.host = host
        self.port = port
        self.rsa_public_key_serve = rsa_public_key_serve
        self.pgp_public_key_serve = pgp_public_key_serve
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)

    def receive_request(self):
        client_socket, client_address = self.socket.accept()
        request_data = client_socket.recv(3060)

        # Decrypt the request using the server's private key
        decrypted_request = rsa_private_key_serve.decrypt(encrypted_request, rsa_private_key_serve).decode('utf-8')
        
        # Parse the decrypted request
        request_parts = decrypted_request.split('|')

        if len(request_parts) == 3:
            url_format = request_parts[0].strip()
            rsa_public_key_serve = request_parts[1].strip()
            encrypted_url = request_parts[2].strip()
            #pgp_public_key_client = request_parts[3].strip()
            
           # Verify the PGP signature
            if self.verify_pgp_signature(pgp_sing_data, f"{url_format}|{rsa_public_key}|{encrypted_url}"):
                if pgp_public_key_client == self.pgp_public_key_client:
                    return client_socket, encrypted_url
                else:
                    return None, "Invalid Public Key"

            if method == "CUSTOM_METHOD" and self.verify_pgp_signature(pgp_signature, f"{url}|{rsa_public_key_serve}|{encrypted_data}"):
                if pgp_public_key_serve == self.pgp_public_key_serve:
                    return client_socket, custom_command, url, encrypted_data
                else:
                    return None, "Invalid "
        
          if url_format.startswith("webs:") and self.verify_pgp_signature(pgp_signature, f"{url}|{rsa_public_key}|{encrypted_url}|"):
                if pgp_public_key_serve == self.gpg_public_key_serve:
                    return client_socket, encrypted_url
                else:
                    return None, "Invalid "
            
            # Verify the PGP signature
            if self.verify_pgp_signature(pgp_signature, f"{url_format}|{rsa_public_key_serve}|{encrypted_url}|"):
                if pgp_public_key_serve == self.pgp_public_key_serve:
                    return client_socket, encrypted_url
                else:
                    return None, "Invalid "
            

    def send_response(self, custom_command, client_socket, response_data):
            
        # Sign the response with the server's private PGP key
        # Encrypt the response with the 
       pgp_sig = self.sign_pgp_data(f"{request_data}|{custom_response}|") #correcao
        encrypted_request = rsa_public_key_client.encrypt(f"|{pgp_sig}|".encode('utf-8'),self.rsa_public_key_client)
       
       self.socket.sendall(encrypted_request)
        
        client_socket.sendall(encrypted_response)
        client_socket.close()
        
        data.files(f"{request_data}|{custom_response}|{custom_command}|{response_data}|")
        
        
            
         
        if self.verify_pgp_signature(pgp_sing_data):
            return pgp_sing_data 
        else:
            return "Invalid PGP Signature"
       # client_socket.close()

    def verify_pgp_signature(self, signature, data, pgp_public_key): #correcaoo
        try:
        # Verify the PGP signature using the client's public PGP key
        # Return True if the signature is valid, False otherwise
                # Lógica de verificação da assinatura PGP
        #from_blob(data) 
        public_key = pgp_public_key_client
        signature = pgpy.PGPSignature.form_file(data) 
        data = data.files(f"{request_data}|{custom_response}|{custom_command}|{response_data}|")
         
        
        public_key.verify(signature) 
                print("A assinatura PGP é válida.") 
                except pgpy.errors.PGPError: 
                    print("assinatura PGP invalida")

    def sign_pgp_data(self, request_data, custom_response, custom_command,response_data): #correcao
        # Sign the data with the server's private PGP key
        # Return the PGP signature
        # Lógica de assinatura PGP
    try:
        # Carregar a chave privada
        key, _ = pgpy.PGPKey.from_blob(gpg_private_key_serve)
        key.unlock(private_key_passphrase)

        # Criar a mensagem com os dados
        message = PGPMessage.new(f"{request_data}|{custom_response}|{custom_command}|{response_data}|", sensitive=True) 

        # Assinar a mensagem
        signature = signed_message
        signed_message = key.sign(message)

        # Retornar a assinatura PGP
        return signature
    except PGPError as e:
        print("Erro ao criar a assinatura PGP:", e)

class WEBDClient:
    def__init__(self, host, port, public_key, pgp_public_key):
        self.host = host
        self.port = port
        self.rsa_public_key = rsa_public_key_client
        self.pgp_public_key = pgp_public_key_client
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_request(self, request_data): #correcao
        # Sign the request with the client's private PGP key
        # Encrypt the request with the server's public RSA key
        def send_request(self, request_data, custom_response, custom_command, response_data):
        pgp_sign_data = self.sign_pgp_data(request_data, custom_response, custom_command, response_data)
        encrypted_request = self.rsa_public_key.encrypt(f"{request_data}|{custom_response}|{pgp_sign_data}".encode('utf-8'))
        self.socket.sendall(encrypted_request)

    def receive_response(self):
        encrypted_response = self.socket.recv(3060)
        decrypted_response = rsa_private_key_client.decrypt(encrypted_response).decode('utf-8')

        response_parts = decrypted_response.split('|')
        url = response_parts[0]
        rsa_public_key_serve = response_parts[1]
        pgp_sign_data = response_parts[2].strip()
        #pgp_public_key = response_parts[3].strip() 
        

        if self.verify_pgp_signature(pgp_sing_data, pgp_public_key_serve): #correcao
            return custom_response
        else:
            return "Invalid PGP Signature"

    def verify_pgp_signature(self, signature, pgp_public_key_serve): #correcao
        # Verify the PGP signature using the server's public PGP key
        # Return True if the signature is valid, False otherwise
        # Lógica de verificação da assinatura 
        try: 
         
         
         public_key = pgp_public_key_serve
            pgp_signature = pgpy.PGPSignature.from_blob(signature)
            
            public_key.verify(pgp_signature)
            print("A assinatura PGP é válida.")
        except pgpy.errors.PGPError:
            print("Assinatura PGP inválida")

    def sign_pgp_data(self, data, private_key_passphrase, private_key): #correcao
        # Sign the data with the client's private PGP key
        # Return the PGP signature
    try:
        # Carregar a chave privada
        key, _ = pgpy.PGPKey.from_blob(pgp_private_key)
        key.unlock(pgp_private_key_passphrase)

        # Criar a mensagem com os dados
       message = pgpy.PGPMessage.new(f"{request_data}|{custom_response}|{custom_command}|{response_data}", sensitive=True)
       # Assinar a mensagem
       signature = key.sign(message)
        
        

        # Retornar a assinatura PGP
        return signature
    except PGPError as e:
        print("Erro ao criar a assinatura PGP:", e)

        
    def close_connection(self):
        self.socket.close()
