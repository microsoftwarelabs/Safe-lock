package app.safe_lock.secure_messenger;

import org.bouncycastle.crypto.AsymmetricCipherKeyPair;
import org.bouncycastle.crypto.params.ParametersWithRandom;
import org.bouncycastle.pqc.crypto.mceliece.*;
import org.bouncycastle.pqc.math.linearalgebra.*;
import org.bouncycastle.pqc.jcajce.provider.mceliece.BCMcElieceCCA2PrivateKey;
import org.bouncycastle.pqc.jcajce.provider.mceliece.BCMcElieceCCA2PublicKey;
import org.bouncycastle.pqc.crypto.sphincsplus.SPX;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.util.Base64;

public class McElieceService {
    private static final SecureRandom RAND = new SecureRandom();
    private static final int SPHINCS_HASH_LENGTH = 32; // Ajuste conforme necessário para SPHINCS+

    public AsymmetricCipherKeyPair generateKeyPair() {
        McElieceCCA2KeyPairGenerator kpg = new McElieceCCA2KeyPairGenerator();
        McElieceCCA2Parameters params = new McElieceCCA2Parameters();
        McElieceCCA2KeyGenerationParameters genParam = new McElieceCCA2KeyGenerationParameters(RAND, params);
        kpg.init(genParam);
        return kpg.generateKeyPair();
    }

    public McElieceCCA2PublicKeyParameters recoverPubFromPriv(McElieceCCA2PrivateKeyParameters priv) {
        GF2mField field = priv.getField();
        PolynomialGF2mSmallM gp = priv.getGoppaPoly();
        GF2Matrix h = GoppaCode.createCanonicalCheckMatrix(field, gp);
        Permutation p = priv.getP();
        GF2Matrix hp = (GF2Matrix) h.rightMultiply(p);
        GF2Matrix sInv = hp.getLeftSubMatrix();
        GF2Matrix s = (GF2Matrix) sInv.computeInverse();
        GF2Matrix shp = (GF2Matrix) s.rightMultiply(hp);
        GF2Matrix m = shp.getRightSubMatrix();

        GoppaCode.MaMaPe mmp = new GoppaCode.MaMaPe(sInv, m, p);
        GF2Matrix shortH = mmp.getSecondMatrix();
        GF2Matrix shortG = (GF2Matrix) shortH.computeTranspose();
        // generate public key
        return new McElieceCCA2PublicKeyParameters(
                priv.getN(), gp.getDegree(), shortG,
                priv.getDigest());
    }

    public String encrypt(String message, McElieceCCA2PublicKeyParameters pub) throws Exception {
        ParametersWithRandom params = new ParametersWithRandom(pub, RAND);
        McElieceFujisakiCipher cipher = new McElieceFujisakiCipher();
        cipher.init(true, params);
        byte[] ciphertext = cipher.messageEncrypt(message.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(ciphertext); // Encode para Base64
    }

    public String decrypt(String base64Ciphertext, McElieceCCA2PrivateKeyParameters priv) throws Exception {
        byte[] ciphertext = Base64.getDecoder().decode(base64Ciphertext); // Decode de Base64
        McElieceFujisakiCipher cipher = new McElieceFujisakiCipher();
        cipher.init(false, priv);
        byte[] decryptedText = cipher.messageDecrypt(ciphertext);
        return new String(decryptedText, StandardCharsets.UTF_8);
    }

    // Função de hash usando SPHINCS+
    public String hash(String data) {
        SPX spx = new SPX();
        byte[] hashBytes = spx.hash(data.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(hashBytes);
    }

    // Escreve a saída no arquivo especificado
    public void writeToFile(String fileName, String content) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write(content);
        }
    }

    // Lê a entrada do arquivo especificado
    public String readFromFile(String fileName) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            StringBuilder content = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
            return content.toString().trim();
        }
    }

    // Função de execução para simular comandos recebidos
    public void executeCommands() {
        try {
            String command = readFromFile("command.txt");
            switch (command) {
                case "GENERATE_KEYS":
                    AsymmetricCipherKeyPair keyPair = generateKeyPair();
                    String publicKey = Base64.getEncoder().encodeToString(keyPair.getPublic().getEncoded());
                    String privateKey = Base64.getEncoder().encodeToString(keyPair.getPrivate().getEncoded());
                    writeToFile("publicKey.txt", publicKey);
                    writeToFile("privateKey.txt", privateKey);
                    break;
                case "HASH":
                    String data = readFromFile("data.txt");
                    String hashed = hash(data);
                    writeToFile("hashed.txt", hashed);
                    break;
                case "ENCRYPT":
                    String message = readFromFile("message.txt");
                    String pubKey = readFromFile("pubKey.txt");
                    String encrypted = encrypt(message, McElieceUtils.decodePublicKey(pubKey));
                    writeToFile("encrypted.txt", encrypted);
                    break;
                case "DECRYPT":
                    String base64Ciphertext = readFromFile("encrypted.txt");
                    String privKey = readFromFile("privKey.txt");
                    String decrypted = decrypt(base64Ciphertext, McElieceUtils.decodePrivateKey(privKey));
                    writeToFile("decrypted.txt", decrypted);
                    break;
                default:
                    writeToFile("error.txt", "Unknown command");
                    break;
            }
        } catch (IOException | Exception e) {
            e.printStackTrace();
        }
    }
}
