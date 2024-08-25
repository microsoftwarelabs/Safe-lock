import * as fs from 'fs';
import * as path from 'path';

export class McEliece {
  private commandFile: string = 'command.txt';
  private dataFile: string = 'data.txt';
  private messageFile: string = 'message.txt';
  private pubKeyFile: string = 'pubKey.txt';
  private privKeyFile: string = 'privKey.txt';
  private resultFile: string = 'result.txt';

  constructor() {}

  private writeFile(fileName: string, content: string): void {
    fs.writeFileSync(fileName, content, 'utf8');
  }

  private readFile(fileName: string): string {
    return fs.readFileSync(fileName, 'utf8').trim();
  }

  public async generateKeys(): Promise<void> {
    this.writeFile(this.commandFile, 'GENERATE_KEYS');
    // Espera que o Java processe o comando e gere os arquivos de chave
    await this.waitForFile('publicKey.txt');
    await this.waitForFile('privateKey.txt');
  }

  public async hash(data: string): Promise<void> {
    this.writeFile(this.commandFile, 'HASH');
    this.writeFile(this.dataFile, data);
    // Espera que o Java processe o comando e gere o hash
    await this.waitForFile('hashed.txt');
  }

  public async encrypt(data: string, publicKey: string): Promise<void> {
    this.writeFile(this.commandFile, 'ENCRYPT');
    this.writeFile(this.messageFile, data);
    this.writeFile(this.pubKeyFile, publicKey);
    // Espera que o Java processe o comando e gere o texto criptografado
    await this.waitForFile('encrypted.txt');
  }

  public async decrypt(encryptedData: string, privateKey: string): Promise<void> {
    this.writeFile(this.commandFile, 'DECRYPT');
    this.writeFile(this.privKeyFile, privateKey);
    this.writeFile(this.resultFile, encryptedData);
    // Espera que o Java processe o comando e gere o texto descriptografado
    await this.waitForFile('decrypted.txt');
  }

  private waitForFile(fileName: string): Promise<void> {
    return new Promise((resolve, reject) => {
      const checkFile = () => {
        if (fs.existsSync(fileName)) {
          resolve();
        } else {
          setTimeout(checkFile, 100);
        }
      };
      checkFile();
    });
  }
}
