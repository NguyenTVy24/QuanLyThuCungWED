// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract ThuCung{
    address public owner;
    address public immutable father;
    address public immutable mother;
    bytes32 hashInformation;
    /*string information;
    string color;
    string birthday;
    string soMuiTiem; */
    event OriginUpdated(bytes32 _information, address updatedBy);
    constructor(address _father,address _mother,string memory _information){
        owner = msg.sender;
        father = _father;
        mother = _mother;
        hashInformation = keccak256(abi.encodePacked(msg.sender,_father, _mother, _information));
    }
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }
    function updateinformation(address _owner,string memory _information) public onlyOwner {
        hashInformation = keccak256(abi.encodePacked(_owner,father, mother, _information));
        owner = _owner;
        emit OriginUpdated(hashInformation, msg.sender);
    }
    function getmother() public view returns(address){
        return mother;
    }
    function getfather() public view returns(address){
        return father;
    }
    function getMyInformation(address _owner,address _father,address _mother,string memory _information) public view returns(bool){
        return hashInformation == keccak256(abi.encodePacked(_owner,_father, _mother, _information));
    }
}