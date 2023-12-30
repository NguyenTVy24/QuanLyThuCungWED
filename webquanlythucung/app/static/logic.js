function newSmartContract(information){
    var web3 = new Web3();
    const contract = new web3.eth.Contract(abi);
    const account = web3.eth.accounts.create();
    // thông tin cân thiết lập
    const father = '0x1234567890123456789012345678901234567890';
    const mother = '0x1234562345678901234789015678901234567890';
    ///////////////////////
    contract.deploy({
        data: '0x' + bytecode,
        arguments: [father,mother,information],
    })
    .send({
        from: account.address,
        gas: '4700000',  // Gas limit
    })
    .then(newContractInstance => {
        console.log('Contract deployed at:', newContractInstance.options.address); 
    })
    .catch(error => {
        console.error('Error deploying contract:', error);
    });
}
function interfaceSmartContract(){
    const Web3 = require('web3');
    const fs = require('fs');
    const web3 = new Web3('http://localhost:8545');
    const contractSourceCode = fs.readFileSync('thucung.sol', 'utf-8');
    const contractCompiled = web3.eth.compileSolidity(contractSourceCode);
    const contractABI = contractCompiled.SimpleStorage.info.abiDefinition;
    // dữ liệu cần điền vào
    const contractAddress = "00000000000000000000";
    ///////////////////////
    const contract = new web3.eth.Contract(contractABI, contractAddress);
    /////một sô methods thông hợp đồng
    contract.methods.getMyInformation().call()
    .then(result => {
        // thông tin cần điều chỉnh
        console.log('Result from the contract:', result);
    })
    .catch(error => {
        console.error('Error calling the contract method:', error);
    });
    //
    contract.methods.getmother().call()
    .then(result => {
        // thông tin cần điều chỉnh
        console.log('Result from the contract:', result);
    })
    .catch(error => {
        console.error('Error calling the contract method:', error);
    });
    //
    contract.methods.getfather().call()
    .then(result => {
        // thông tin cần điều chỉnh
        console.log('Result from the contract:', result);
    })
    .catch(error => {
        console.error('Error calling the contract method:', error);
    });
    //thông tin cần cung cấp
    const owner = "00000000000000000000";
    const information = "afasdddddddd";
    /////
    contract.methods.updateinformation(owner,information).call()
    .then(result => {
        // thông tin cần điều chỉnh
        console.log('Result from the contract:', result);
    })
    .catch(error => {
        console.error('Error calling the contract method:', error);
    });
}
function sendPostRequest(value) {
    // Tạo dữ liệu JSON từ các trường input
    var data = {
        idmetamaxk: value
    };

    // Gửi POST request
    fetch('/connectedMetaMask/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(response_data => {
        // Xử lý dữ liệu từ response
        console.log("da ket noi:"+response_data);
    })
    .catch(error => {
        // Xử lý lỗi
        console.error('Error:', response_data);
    });
}
