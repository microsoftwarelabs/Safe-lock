package app.safe_lock.secure_messenger;

import io.flutter.embedding.android.FlutterActivity;
import io.flutter.embedding.engine.FlutterEngine;
import io.flutter.plugin.common.MethodChannel;

public class MainActivity extends FlutterActivity {
    private static final String CHANNEL = "app.safe_lock.secure_messenger/crypto";
    private CryptographySystem cryptoSystem;

    @Override
    public void configureFlutterEngine(FlutterEngine flutterEngine) {
        super.configureFlutterEngine(flutterEngine);
        try {
            cryptoSystem = new CryptographySystem();

            new MethodChannel(flutterEngine.getDartExecutor().getBinaryMessenger(), CHANNEL)
                .setMethodCallHandler(
                    (call, result) -> {
                        if (call.method.equals("generateAndEncryptData")) {
                            byte[] data = call.argument("data");
                            try {
                                cryptoSystem.generateAndEncryptData(data);
                                result.success("Data encrypted successfully");
                            } catch (Exception e) {
                                result.error("UNAVAILABLE", "Failed to encrypt data.", null);
                            }
                        } else if (call.method.equals("decryptData")) {
                            byte[] data = call.argument("data");
                            try {
                                byte[] decryptedData = cryptoSystem.decryptData(data);
                                result.success(decryptedData);
                            } catch (Exception e) {
                                result.error("UNAVAILABLE", "Failed to decrypt data.", null);
                            }
                        } else {
                            result.notImplemented();
                        }
                    }
                );
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
