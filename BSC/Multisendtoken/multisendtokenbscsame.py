from web3 import Web3, HTTPProvider
import json
import logging
import datetime 
import threading
import asyncio
import requests
import time
import os
import sys
import ctypes
import pyperclip as pc

bsc = "https://bsc-rpc.gateway.pokt.network/"
web3 = Web3(Web3.HTTPProvider(bsc))

ctypes.windll.kernel32.SetConsoleTitleW("Multisender Token BSC")
print('multisender token bsc with same amount')
print('you can custom to send to a lot address')
print('this example send to 2 address')
print('you need gasfee bnb to send token to other address')

#connecting web3
if  web3.isConnected() == True:
    print("web3 connected...\n")
else :
    print("error connecting please try again...")

sender = web3.toChecksumAddress(input("Enter your address sender 0x...: "))
#sender = web3.toChecksumAddress('0x0') #send from this address
senderkey = input("Enter your privatekey sender abcde12345...: ")
#senderkey = 'abcd1234' #senderkey
recipient1 = web3.toChecksumAddress(input("Enter your address recipient1 0x...: "))
recipient2 = web3.toChecksumAddress(input("Enter your address recipient2 0x...: "))
#recipient1 = web3.toChecksumAddress('0x0') #to this address
#recipient2 = web3.toChecksumAddress('0x0') #to this address
all_recipient = [recipient1, recipient2] #ex send to 2 address, if want more send to a lot address, you need modif it
tokenaddr = web3.toChecksumAddress(input('Enter token address 0x...: '))
contract_address = web3.toChecksumAddress('0xd152f549545093347a162dce210e7293f1452150') #Disperse.app
#gasAmount = 50000 #gas limit // change if transaction fail
#gasPrice = 1 #gas price
chainId = 56 

abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
tokenabi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address=contract_address, abi=abi)
token_contract = web3.eth.contract(address=tokenaddr, abi=tokenabi)
tokenName = token_contract.functions.name().call()
tokenSymbol = token_contract.functions.symbol().call()

#Get balance account
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'BNB')
    #Get token balance account
    token_balance = token_contract.functions.balanceOf(sender).call()
    balance_token = web3.fromWei(token_balance, 'ether')
    print('Token Balance' ,balance_token, tokenSymbol)
    
UpdateBalance()

nonce = web3.eth.getTransactionCount(sender)

token_approve = token_contract.functions.balanceOf(sender).call()

#estimate gas limit approve
gas_approve = token_contract.functions.approve(contract_address, token_approve).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gasPrice': web3.eth.gas_price,
    'nonce': nonce
})
gasApprove = web3.eth.estimateGas(gas_approve)

#Approve
Approve = token_contract.functions.approve(contract_address, token_approve).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gas': gasApprove,
    'gasPrice': web3.eth.gas_price,
    'nonce': nonce
})

sign_approve = web3.eth.account.sign_transaction(Approve, senderkey)
web3.eth.send_raw_transaction(sign_approve.rawTransaction)
print('Approved spender token... wait 10 second...')
time.sleep(10)

inputamount = float(input("Enter amount of token you want to send: ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount = web3.toWei(float(inputamount), 'ether')
amountall = [amount, amount] #2 address, if want more send to a lot address, you need modif it

#estimate gas limit contract
nonce2 = web3.eth.getTransactionCount(sender)
gas_tx = contract.functions.disperseToken(tokenaddr, all_recipient, amountall).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': nonce2
})
gasAmount = web3.eth.estimateGas(gas_tx)

token_tx = contract.functions.disperseToken(tokenaddr, all_recipient, amountall).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'gas': gasAmount,
    'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
    'nonce': nonce2
})

#sign the transaction
sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
#send transaction
tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

#get transaction hash
txid = str(web3.toHex(tx_hash))
print('Transaction Success TX-ID Copied To Clipboard')
print('https://bscscan.com/tx/'+txid)
pc.copy('https://bscscan.com/tx/'+txid)
print('update current balance in 30 second...')
time.sleep(30)
UpdateBalance() #get latest balance
print('will close automatically in 30 second...')
time.sleep(30)