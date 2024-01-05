from web3 import Web3, AsyncWeb3

def context():
    infura_url = "https://mainnet.infura.io/v3/190bfdae5b0f4c5da3db86bb58b410b9"
    web3 = Web3(Web3.HTTPProvider(infura_url))
    print(web3.is_connected())

