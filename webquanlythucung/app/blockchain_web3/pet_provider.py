import json
import os.path
import uuid

from eth_typing import Address

from app.blockchain_web3.provider import Web3Provider
from django.conf import settings


class PetProvider(Web3Provider):
        
    def __init__(self, path_abi=None, chain_id=None, web3_provider=None, address_contract=None):
        path_abi = path_abi if path_abi else os.path.join(os.getcwd(), "app/abi/pet.txt")
        with open(path_abi, 'r', encoding='utf-8') as f:
            abi = f.read()

        factory_abi = json.loads(abi)
        web3_provider = web3_provider if web3_provider else settings.WEB3_PROVIDER
        address_contract = address_contract if address_contract else settings.ADDRESS_CONTRACT_ACTOR_MANAGER
        super().__init__(web3_provider, address_contract)
        self.chain_id = chain_id if chain_id else settings.CHAIN_ID
        self.contract = self.w3.eth.contract(address=address_contract, abi=factory_abi)

    def create_actor(self, user_id: str, address, role, name, real_address,key):
        function = self.contract.functions.create(user_id, Address(address), role, name, real_address)
        return self.sign_and_send_transaction(function,key)

    def update_pet(self, information, real_address,key):
        function = self.contract.functions.updateinformation(real_address, information)
        return self.sign_and_send_transaction(function,key)

    def get_pet_MyInformation(self,owner,father,mother,information):
        return self.contract.functions.getMyInformation(owner,father,mother,information).call()
    
    @staticmethod
    def convert_data_user(data):
        return {
            'owner': data[0],
            'father': data[1],
            "mother": data[2],
            'hashInformation': data[3]
        }
