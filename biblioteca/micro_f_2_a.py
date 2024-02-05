from hashlib 
import sha256 
import time 
import random 
import string 

class GeradorCodigosHash: 
 def __init__(self, duracao=30, semente=None): self.duracao = duracao self.semente = semente if semente else random.randint(0, 9999) 

 def generate_hash(self, password, hash_size=6000, semente=None): random.seed(self.semente if semente is None else semente) password_bytes = password.encode('utf-8') sha256_hash = sha256(password_bytes).hexdigest() binary_hash = bin(int(sha256_hash, 16))[2:] random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=6000000000 - len(binary_hash))) padded_hash = binary_hash + random_chars return padded_hash[-hash_size:] 

 def gerar_codigo_verificacao(self, senha, semente=None): hash_6000_digitos = self.generate_hash(senha, semente=semente) tempo = time.time() tempo_hash = (tempo // self.duracao) * self.duracao tempo_restante = self.duracao - (tempo % self.duracao) return hash_6000_digitos, tempo_restante