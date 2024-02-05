# Safe-lock
Blockchain-based online chat application
aplicativo de chat online baseado em blockchain 

modo de uso da bicicleta microf2a 

'''
from sua_biblioteca import GeradorCodigosHash  # Substitua "sua_biblioteca" pelo nome do arquivo onde está a classe GeradorCodigosHash

# Criando uma semente própria
minha_semente = 12345  # Substitua pelo valor da sua semente

# Criando uma instância da classe GeradorCodigosHash com duração de 5 segundos e a semente própria
gerador = GeradorCodigosHash(duracao=5, semente=minha_semente)

# Gerando um código de verificação de 300 caracteres aleatórios com a semente própria
codigo, tempo_restante = gerador.gerar_codigo_verificacao('sua_senha_aqui', semente=minha_semente)

print(f'Código de verificação: {codigo}')
print(f'Tempo restante: {tempo_restante} segundos')

'''