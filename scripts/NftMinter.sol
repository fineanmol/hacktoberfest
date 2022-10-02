pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MyFts is ERC721URIStorage,Ownable{
    using Counters for Counters.Counter;
    
    Counters.Counter private _tokenIds;
    constructor() ERC721("FineAnmol","BNFT"){}

    function mintNFT(address recipients,string memory tokenURI) public onlyOwner returns(uint256){
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(recipients,newItemId);
        _setTokenURI(newItemId,tokenURI);
        return newItemId;
    } 
}

