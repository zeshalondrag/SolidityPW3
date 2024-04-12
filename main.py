from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0) 

contract = w3.eth.contract(address=contract_address, abi=abi)   

print(contract.address)
print(f"Баланс смарт-контракта: {w3.eth.get_balance(contract_address)}")
print(f"Баланс аккаунат 1: {w3.eth.get_balance('0xD50085e29281bF83a15dfa5231bcF9b4EfeA4B2A')}")
print(f"Баланс аккаунат 2: {w3.eth.get_balance('0x656D89e214027065ec96341662E8c55486fBc11c')}")
print(f"Баланс аккаунат 3: {w3.eth.get_balance('0xAb5411bb9B24e2c7b736109acC213E28026bD932')}")
print(f"Баланс аккаунат 4: {w3.eth.get_balance('0x5746C4CdAC92D119D0F4E9412cCed9845752e525')}")
print(f"Баланс аккаунат 5: {w3.eth.get_balance('0xB392522C5640421d0D074770a00Fc40707d264D5')}")