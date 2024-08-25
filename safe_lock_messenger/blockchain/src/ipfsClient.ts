import { create } from 'ipfs-http-client';

export class IPFSClient {
  private client;

  constructor() {
    this.client = create({ url: 'https://ipfs.infura.io:5001/api/v0' });
  }

  public async upload(data: string): Promise<string> {
    const { path } = await this.client.add(data);
    return path;
  }
}
