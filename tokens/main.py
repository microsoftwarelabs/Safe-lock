from web3 import Web3
from eth_account import Account
import json

# Replace with your private key (Alterar para a chave do cliente (ainda não sei a forma que vamos obtela))
private_key = 'your_private_key_here'

# Replace with the contract address of BriseBrigide
brise_brigide_contract_address = 'brise_brigide_contract_address_here'

# Replace with the recipient address for the token sale proceeds
recipient_address = 'recipient_address_here'

# Set up the Web3 connection to the Ethereum network
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your_project_id_here'))

# Load the D'CENT wallet
account = Account.from_key(private_key)

# Load the ABI of BriseBrigide contract
with open('output/BriseBrigide.abi', 'r') as f:
    abi = json.load(f)

# Set up the BriseBrigide contract
brise_brigide_contract = web3.eth.contract(address=brise_brigide_contract_address, abi=abi)

# Set up the token sale parameters
token_sale_amount = web3.toWei(1, 'ether')  # Replace with the desired amount of tokens to sell
token_decimals = 18  # Replace with the actual number of decimal places for the token

# Get the token balance of the D'CENT wallet
token_balance = brise_brigide_contract.functions.balanceOf(account.address).call() / (10 ** token_decimals)

# Ensure that the D'CENT wallet has enough tokens to sell
if token_balance < token_sale_amount:
    print('Insufficient token balance')
    exit()

# Approve the token sale
approve_tx = brise_brigide_contract.functions.approve(recipient_address, token_sale_amount).buildTransaction({
    'from': account.address,
    'gas': 50000,
    'gasPrice': web3.toWei('10', 'gwei'),
    'nonce': web3.eth.getTransactionCount(account.address),
})
signed_approve_tx = account.sign_transaction(approve_tx)
tx_hash = web3.eth.send_raw_transaction(signed_approve_tx.rawTransaction)
web3.eth.wait_for_transaction_receipt(tx_hash)

# Execute the token sale
sell_tx = brise_brigide_contract.functions.transferFrom(account.address, recipient_address, token_sale_amount).buildTransaction({
    'from': account.address,
    'gas': 50000,
    'gasPrice': web3.toWei('10', 'gwei'),
    'nonce': web3.eth.getTransactionCount(account.address),
})
signed_sell_tx = account.sign_transaction(sell_tx)
tx_hash = web3.eth.send_raw_transaction(signed_sell_tx.rawTransaction)
web3.eth.wait_for_transaction_receipt(tx_hash)

print('Token sale completed')
