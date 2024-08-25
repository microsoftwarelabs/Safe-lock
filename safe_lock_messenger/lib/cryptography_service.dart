import 'dart:typed_data';
import 'package:flutter/services.dart';

class CryptographyService {
  static const platform = MethodChannel('app.safe_lock.secure_messenger/crypto');

  Future<void> generateAndEncryptData(Uint8List data) async {
    try {
      await platform.invokeMethod('generateAndEncryptData', {'data': data});
    } on PlatformException catch (e) {
      print("Failed to encrypt data: '${e.message}'.");
    }
  }

  Future<Uint8List> decryptData(Uint8List encryptedData) async {
    try {
      final Uint8List result = await platform.invokeMethod('decryptData', {'data': encryptedData});
      return result;
    } on PlatformException catch (e) {
      print("Failed to decrypt data: '${e.message}'.");
      return Uint8List(0);
    }
  }
}
