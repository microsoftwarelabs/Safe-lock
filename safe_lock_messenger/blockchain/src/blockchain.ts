import { NodeVM } from 'vm2';
import * as crypto from 'crypto';
import { SmartContract } from './smartContract';
import { IPFSClient } from './ipfsClient';
import { McEliece } from './mceliece';

interface NFT {
  id: string;
  owner: string;
  metadata: string;
}

interface MVSOptions {
  timeout?: number;
  allowedModules?: string[];
  allowedApis?: string[];
}

interface Block {
  index: number;
  timestamp: number;
  data: string;
  previousHash: string;
  hash: string;
  nonce: number;
}

interface Transaction {
  from: string;
  to: string;
  amount: number;
  token: string;
  data: string;
}

interface Token {
  name: string;
  symbol: string;
  totalSupply: number;
  decimals: number;
}

interface SLB {
  balance: number;
  transactions: Transaction[];
}

interface IMAG {
  balance: number;
  nfts: NFT[];
}

interface FORT {
  balance: number;
  ethBalance: number;
}

interface NIT {
  balance: number;
  maticBalance: number;
}

interface LOW {
  balance: number;
  storage: {
    [key: string]: string;
  };
}

export class Blockchain {
  private chain: Block[] = [];
  private mceliece: McEliece;
  private contracts: SmartContract[] = [];
  private mvs: MVS;
  private ipfsClient: IPFSClient;
  private mceliece: McEliece;
  private slb: SLB;
  private imag: IMAG;
  private fort: FORT;
  private nit: NIT;
  private low: LOW;

  constructor() {
    this.mvs = new MVS({
      timeout: 5000,
      allowedModules: [], // Nenhum módulo externo permitido
      allowedApis: ['crypto'], // Apenas APIs necessárias
    });
    this.ipfsClient = new IPFSClient();
    this.mceliece = new McEliece();
    this.slb = { balance: 0, transactions: [] };
    this.imag = { balance: 0, nfts: [] };
    this.fort = { balance: 0, ethBalance: 0 };
    this.nit = { balance: 0, maticBalance: 0 };
    this.low = { balance: 0, storage: {} };
    this.mceliece = new McEliece();
    this.createGenesisBlock();
  }

  private createGenesisBlock() {
    const genesisBlock: Block = {
      index: 0,
      timestamp: Date.now(),
      data: "Genesis Block",
      previousHash: "0",
      hash: this.calculateHash("Genesis Block", "0"),
      nonce: 0,
    };
    this.chain.push(genesisBlock);
  }

  public deployContract(contract: SmartContract) {
    if (this.isContractValid(contract)) {
      this.contracts.push(contract);
    } else {
      console.error('Invalid contract');
    }
  }

  private isContractValid(contract: SmartContract): boolean {
    // Implementar lógica de validação de contrato
    // Exemplo: Verificar se o código do contrato não contém funções perigosas
    return true;
  }

  public createNFT(id: string, metadata: any) {
    const nft: NFT = { id, owner: "initialOwner", metadata };
    this.imag.nfts.push(nft);
    console.log(`NFT Created: ${JSON.stringify(nft)}`);
  }

  public destroyNFT(id: string) {
    if (this.imag.nfts.find((nft) => nft.id === id)) {
      this.imag.nfts = this.imag.nfts.filter((nft) => nft.id !== id);
      console.log(`NFT with ID ${id} destroyed.`);
    } else {
      console.log(`NFT with ID ${id} not found.`);
    }
  }

  public mineBlock(data: string) {
    if (this.isDataValid(data)) {
      const previousBlock = this.chain[this.chain.length - 1];
      const newBlock: Block = {
        index: previousBlock.index + 1,
        timestamp: Date.now(),
        data,
        previousHash: previousBlock.hash,
        hash: this.calculateHash(data, previousBlock.hash),
        nonce: this.getNonce(),
      };
      this.chain.push(newBlock);
      console.log(`Block mined: ${JSON.stringify(newBlock)}`);
    } else {
      console.error('Invalid block data');
    }

  private isDataValid(data: string): boolean {
    // Implementar lógica de validação de dados
    // Exemplo: Verificar tamanho ou conteúdo dos dados
    return data.length <= 1000; // Exemplo simples de validação
  }
  


}

  public stakeSLB(amount: number) {
    this.slb.balance += amount;
    console.log(`SLB staked: ${amount}`);
  }

  public swapFORT(amount: number) {
    this.fort.balance += amount;
    this.fort.ethBalance += amount;
    console.log(`FORT swapped: ${amount}`);
  }

  public swapNIT(amount: number) {
    this.nit.balance += amount;
    this.nit.maticBalance += amount;
    console.log(`NIT swapped: ${amount}`);
  }

  public storeData(data: string) {
    if (data.length <= 800000) {
      const encryptedData = this.mceliece.encrypt(data);
      const cid = this.ipfsClient.upload(encryptedData);
      this.low.storage[cid] = encryptedData;
      this.low.balance += 1;
      console.log(`Data stored: ${cid}`);
    } else {
      console.log(`Data too large`);
    }
  }

  public getGasPrice(): number {
    return 10;
  }

  public storeConfig(config: any) {
    console.log(`Config stored: ${JSON.stringify(config)}`);
  }

  // Modificado para usar McEliece em vez de SHA-256
  private calculateHash(data: string, previousHash: string): string {
    // Criptografar a concatenação de dados e hash anterior usando McEliece
    const combinedData = `${data}${previousHash}`;
    const encryptedData = this.mceliece.encrypt(combinedData);
    
    // Converter os dados criptografados para uma string hexadecimal para o hash
    return this.convertToHex(encryptedData);
  }

  private convertToHex(data: Uint8Array): string {
    return Array.prototype.map.call(new Uint8Array(data), x => ('00' + x.toString(16)).slice(-2)).join('');
  }

  private getNonce(): number {
    return this.chain.length;
  }

  private getNonce(): number {
    return this.chain.length;
  }

  public getSLBBalance(): number {
    return this.slb.balance;
  }

  public getIMAGBalance(): number {
    return this.imag.balance;
  }

  public getFORTBalance(): number {
    return this.fort.balance;
  }

  public getNITBalance(): number {
    return this.nit.balance;
  }

  public getLOWBalance(): number {
    return this.low.balance;
  }

  public getNFTs(): NFT[] {
    return this.imag.nfts;
  }

  public getBlockChain(): Block[] {
    return this.chain;
  }

  public getContracts(): SmartContract[] {
    return this.contracts;
  }
}


class MVS {
  private vm: NodeVM;

  constructor(options: MVSOptions = {}) {
    const allowedModules = options.allowedModules || [];
    const allowedApis = options.allowedApis || [];

   this.isolatedConsole = {
      log: (message: any) => this.handleConsoleOutput('log', message),
      error: (message: any) => this.handleConsoleOutput('error', message),
      warn: (message: any) => this.handleConsoleOutput('warn', message),
      info: (message: any) => this.handleConsoleOutput('info', message),
      // Outras funções do console, se necessário
    };

      const allowedModules = options.allowedModules || [];
      const allowedApis = options.allowedApis || [];


    this.vm = new NodeVM({
      sandbox: {
        console: this.isolatedConsole,
      },
      require: {
        external: allowedModules.length > 0 ? allowedModules : false,
        builtin: allowedApis,
      },
      require: {
        external: allowedModules.length > 0 ? allowedModules : false,
        builtin: allowedApis,
      },
      wrapper: 'none', // Não permitir a execução de código não protegido
      timeout: options.timeout || 1000, // Timeout padrão
      console: 'inherit', // Pode ser 'inherit' ou 'none'
    });
  }


  // Função para lidar com a saída do console
  private handleConsoleOutput(type: string, message: any) {
    // Implementar como você deseja tratar a saída do console
    // Por exemplo, registrar em um arquivo, enviar a um serviço de monitoramento, etc.
    console[type](`[Console ${type}] ${message}`);
  }


  public execute(code: string, context: any): any {
    try {
      // Cria um ambiente de execução específico para o código do contrato
      return this.vm.run(code, 'sandboxed.vm', context);
    } catch (error) {
      console.error('Execution error:', error);
      throw error;
    }
  }
}


class SmartContract {
  private code: string;
  private mvs: MVS;

  constructor(code: string, mvs: MVS) {
    this.code = code;
    this.mvs = mvs;
  }

  public execute(data: any): any {
    // Opcional: Sanitização do código pode ser feita aqui
    // Exemplo: Verificar se o código do contrato contém apenas funções permitidas

    return this.mvs.execute(this.code, data);
  }
}



class IPFSClient {
  private ipfs: any;

  constructor() {
    this.ipfs = require('ipfs-http-client');
  }

  public upload(data: string): string {
    return this.ipfs.add(data);
  }
}

const blockchain = new Blockchain();

// Example usage
blockchain.deployContract(new SmartContract('console.log("Hello, World!");'));
blockchain.createNFT('nft-1', { name: 'CryptoArt', metadata: 'example metadata' });
blockchain.mineBlock('Transaction data');
blockchain.stakeSLB(100);
blockchain.swapFORT(50);
blockchain.swapNIT(20);
blockchain.storeData('Hello, IPFS!');
console.log(`SLB balance: ${blockchain.getSLBBalance()}`);
console.log(`IMAG balance: ${blockchain.getIMAGBalance()}`);
console.log(`FORT balance: ${blockchain.getFORTBalance()}`);
console.log(`NIT balance: ${blockchain.getNITBalance()}`);
console.log(`LOW balance: ${blockchain.getLOWBalance()}`);
console.log(`NFTs: ${JSON.stringify(blockchain.getNFTs())}`);
console.log(`Blockchain: ${JSON.stringify(blockchain.getBlockChain())}`);
console.log(`Contracts: ${JSON.stringify(blockchain.getContracts())}`);
