export interface NFT {
  id: string;
  owner: string;
  metadata: string;
}

export class NFTManager {
  private nfts: NFT[] = [];

  constructor() {
    // Carregar NFTs existentes, se necessário
  }

  public createNFT(id: string, owner: string, metadata: string): NFT {
    const nft: NFT = { id, owner, metadata };
    this.nfts.push(nft);
    console.log(`NFT Created: ${JSON.stringify(nft)}`);
    return nft;
  }

  public destroyNFT(id: string): void {
    const nftIndex = this.nfts.findIndex(nft => nft.id === id);
    if (nftIndex > -1) {
      this.nfts.splice(nftIndex, 1);
      console.log(`NFT with ID ${id} destroyed.`);
    } else {
      console.log(`NFT with ID ${id} not found.`);
    }
  }

  public getNFTs(): NFT[] {
    return this.nfts;
  }
}
