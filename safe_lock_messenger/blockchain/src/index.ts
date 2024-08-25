import { Blockchain } from './blockchain';
import { SmartContract } from './smartContract';
import { IPFSClient } from './ipfsClient';

// Inicializa o blockchain e IPFS
const blockchain = new Blockchain();
const ipfsClient = new IPFSClient();

const contract = new SmartContract();
blockchain.deployContract(contract);

console.log("Blockchain e IPFS inicializados.");

// Exemplo de criação e destruição de NFT
blockchain.createNFT("nft-1", { name: "CryptoArt", metadata: "example metadata" });
blockchain.destroyNFT("nft-1");

console.log("NFTs criados e destruídos.");
