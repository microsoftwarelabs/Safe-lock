package app.safe_lock.secure_messenger;

import java.security.SecureRandom;

public class F2A {

    private SecureRandom secureRandom;

    public F2A() {
        secureRandom = new SecureRandom();
    }

    public byte[] generateKey() {
        // Gera uma chave aleatória
        byte[] key = new byte[16];
        secureRandom.nextBytes(key);
        return key;
    }
}
