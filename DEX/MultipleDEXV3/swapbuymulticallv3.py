from web3 import Web3, HTTPProvider
import json
import time
import config

web3 = Web3(Web3.HTTPProvider(config.rpcurl))
chainId = int(config.chainid)

print("Swap Buy DEX V3 | Works Multiple DEX")

#connecting web3
if  web3.isConnected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

sender = config.sender
senderkey = config.pvkey
tokenaddr = config.tokenaddr
contract_router = config.routeraddr
feepool = int(config.feepool)
#============================================================================
contractrouter = web3.eth.contract(address=contract_router, abi=config.router_abi)
token_contract = web3.eth.contract(address=tokenaddr, abi=config.tokenabi)
tokenName = token_contract.functions.name().call()
tokenSymbol = token_contract.functions.symbol().call()
tokenDec = token_contract.functions.decimals().call()
wrapped = contractrouter.functions.WETH9().call()
contractwrapped = web3.eth.contract(address=wrapped, abi=config.tokenabi)

#Get balance account
print('')
def UpdateBalance():
    balance = web3.eth.get_balance(sender)
    balance_bnb = web3.fromWei(balance,'ether')
    print('Your Balance' ,balance_bnb, 'ETH')
    #Get token balance account
    token_balance = token_contract.functions.balanceOf(sender).call() / (10**tokenDec)
    print('Token Balance' ,token_balance, tokenSymbol)
    
UpdateBalance()

print('')
inputamount = float(input("Enter Amount Of You Want To Buy [ETH] : ")) #ex 1 / 0.1 / 0.001 / 0.0001 / 0.00001
amount = web3.toWei(float(inputamount), 'ether')
deadline = int(time.time()) + 1000000

txSwap = contractrouter.encodeABI(fn_name="exactInputSingle", args=[(wrapped, tokenaddr, feepool, sender, amount, 0, 0)])
txCall = [txSwap]

#estimate gas limit contract
gas_tx = contractrouter.functions.multicall(deadline, txCall).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'value': amount,
    'gasPrice': web3.eth.gasPrice, #web3.toWei(gasPrice,'gwei'),
    'nonce': web3.eth.getTransactionCount(sender)
})
gasAmount = web3.eth.estimate_gas(gas_tx)
#print(gasAmount)

#calculate transaction fee
print('')
amountFromWei = web3.fromWei(amount, 'ether')
gasPrice = web3.fromWei(web3.eth.gasPrice, 'gwei')
Caclfee = web3.fromWei(gasPrice*gasAmount, 'gwei')
print('Transaction Fee :' ,Caclfee, 'ETH')
print('Processing Swap Buy :' ,amountFromWei, 'ETH For Token' ,tokenName)

token_tx = contractrouter.functions.multicall(deadline, txCall).buildTransaction({
    'chainId': chainId,
    'from': sender,
    'value': amount,
    'gas': gasAmount,
    'gasPrice': web3.eth.gasPrice, #web3.toWei(gasPrice,'gwei'),
    'nonce': web3.eth.getTransactionCount(sender)
})

#sign the transaction
sign_txn = web3.eth.account.signTransaction(token_tx, senderkey)
#send transaction
tx_hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)

#get transaction hash
txid = str(web3.toHex(tx_hash))
print('')
print('Transaction Success TX-ID Result...')
print(txid)
print('Update Current Balance In 30 Second...')
time.sleep(30)
print('')
UpdateBalance() #get latest balance