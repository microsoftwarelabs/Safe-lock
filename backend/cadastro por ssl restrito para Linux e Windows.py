
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
import datetime
import gnupg
from Crypto.PublicKey import RSA
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


#
########$#$
#


#ssl restrita
def generate_self_signed_cert():
    # Solicitar informações do usuário
    common_name = input("Digite o nome comum (Common Name) para o certificado SSL: ")
    country = input("Digite o código do país (Country): ")
    state = input("Digite o nome do estado (State): ")
    locality = input("Digite o nome da cidade (Locality): ")
    organization = input("Digite o nome da organização (Organization): ")
    email = input("Digite o endereço de e-mail: ")

    # Gerar chave privada RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Gerar certificado
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
        x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS, email)
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True,
    ).sign(private_key, hashes.SHA256())

    # Salvar a chave privada, certificado e chave pública em variáveis
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    cert_pem = cert.public_bytes(serialization.Encoding.PEM)
    public_key_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Retornar a chave privada, certificado e chave pública
    return private_key_pem, cert_pem, public_key_pem

# Chamada da função para gerar o certificado, a chave privada e a chave pública
private_key, cert, public_key = generate_self_signed_cert()

# Exemplo de utilização das variáveis
print("Chave privada:")
print(private_key.decode("utf-8"))
print("\nCertificado:")
print(cert.decode("utf-8"))
print("\nChave pública:")
print(public_key.decode("utf-8"))

#
########$#$
#

#aes
def encrypt_message(message, password):
    backend = default_backend()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    key = kdf.derive(password.encode())

    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return salt, iv, ciphertext


#Decodificação desnecessária
def decrypt_message(salt, iv, ciphertext, password):
    backend = default_backend()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    key = kdf.derive(password.encode())

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_data) + unpadder.finalize()

    return message.decode()

# Exemplo de utilização para gerar a semente pgp
message = pgp2 = cert_pem
password = pgp3 = private_key_pem
salt, iv, ciphertextpgp = encrypt_message(message = pgp2, password = pgp3)
#decrypted_message = decrypt_message(salt, iv, ciphertext, password)

# Exemplo de utilização para gerar a semente sra 
message = rsa2 = public_key_pem
password = rsa3 = cert_pem
salt, iv, ciphertextrsa = encrypt_message(message = rsa2, password = rsa3)
#decrypted_message = decrypt_message(salt, iv, ciphertext, password)

#print("Mensagem original:", message)
#print("Mensagem cifrada:", ciphertext)
#print("Mensagem decifrada:", #decrypted_message)


#
########$#$
#



#pgp
def generate_pgp_keys(seed):
    gpg = gnupg.GPG()

    # Definir a semente personalizada
    os.environ['GPGME_RANDOM_SEED'] = seed

    # Gerar as chaves
    input_data = gpg.gen_key_input(
        key_type="RSA",
        key_length=3080
    )
    key = gpg.gen_key(input_data)

    fingerprint = key.fingerprint
    private_key = str(key)
    public_key = gpg.export_keys(fingerprint)

    return fingerprint, private_key, public_key

# Exemplo de utilização
seed = ciphertextpgp
fingerprint, private_key, public_key = generate_pgp_keys(seed)

print("\nFingerprint da chave:", fingerprint)
print("\nChave privada:", private_key)
print("\nChave pública:", public_key)



#
########$#$
#



#rsa
def generate_rsa_key(seed, key_length=3080):
    random_generator = os.urandom
    rsa_key = RSA.generate(key_length, random_generator, seed)
    return rsa_key

seed = ciphertextrsa
generated_key = generate_rsa_key(seed)

private_key = generated_key.export_key()
public_key = generated_key.publickey().export_key()

with open('private_key.pem', 'wb') as f:
    f.write(private_key)

with open('public_key.pem', 'wb') as f:
    f.write(public_key)

print("\nChave privada gerada e salva em private_key.pem")
print("\nChave pública gerada e salva em public_key.pem")