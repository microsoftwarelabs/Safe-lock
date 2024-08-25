import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  final String baseUrl;

  ApiService(this.baseUrl);

  Future<void> mintNFT(String id, String name, String imageUrl, int fee) async {
    final response = await http.post(
      Uri.parse('$baseUrl/nft/mint'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'id': id,
        'name': name,
        'image_url': imageUrl,
        'fee': fee,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception('Failed to mint NFT');
    }
  }

  Future<void> burnNFT(String id, int fee) async {
    final response = await http.post(
      Uri.parse('$baseUrl/nft/burn'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'id': id,
        'fee': fee,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception('Failed to burn NFT');
    }
  }

  Future<void> swapMaticForMyCoin(String amount) async {
    final response = await http.post(
      Uri.parse('$baseUrl/token_swap/swap_matic_for_mycoin'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'amount': amount,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception('Failed to swap Matic for MyCoin');
    }
  }

  Future<void> swapEthForMy(String amount) async {
    final response = await http.post(
      Uri.parse('$baseUrl/token_swap/swap_eth_for_my'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'amount': amount,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception('Failed to swap ETH for MyCoin');
    }
  }

  Future<void> stakeMyNFTCoin(String amount) async {
    final response = await http.post(
      Uri.parse('$baseUrl/staking/stake_mynftcoin'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'amount': amount,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception('Failed to stake MyNFTCoin');
    }
  }
}
```

### 13. Integrando com o Frontend Flutter

Agora vamos criar a interface do usuário no Flutter para interagir com essas APIs.

**main.dart**

```dart
import 'package:flutter/material.dart';
import 'api_service.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My Blockchain App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final ApiService apiService = ApiService('http://localhost:8080'); // URL da sua API

  final TextEditingController idController = TextEditingController();
  final TextEditingController nameController = TextEditingController();
  final TextEditingController imageUrlController = TextEditingController();
  final TextEditingController feeController = TextEditingController();

  void _mintNFT() async {
    try {
      await apiService.mintNFT(
        idController.text,
        nameController.text,
        imageUrlController.text,
        int.parse(feeController.text),
      );
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('NFT Minted Successfully')));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Error: $e')));
    }
  }

  void _burnNFT() async {
    try {
      await apiService.burnNFT(
        idController.text,
        int.parse(feeController.text),
      );
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('NFT Burned Successfully')));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Error: $e')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('My Blockchain App'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: <Widget>[
            TextField(
              controller: idController,
              decoration: InputDecoration(labelText: 'NFT ID'),
            ),
            TextField(
              controller: nameController,
              decoration: InputDecoration(labelText: 'NFT Name'),
            ),
            TextField(
              controller: imageUrlController,
              decoration: InputDecoration(labelText: 'Image URL'),
            ),
            TextField(
              controller: feeController,
              decoration: InputDecoration(labelText: 'Fee'),
              keyboardType: TextInputType.number,
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _mintNFT,
              child: Text('Mint NFT'),
            ),
            ElevatedButton(
              onPressed: _burnNFT,
              child: Text('Burn NFT'),
            ),
          ],
        ),
      ),
    );
  }
}