import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:myapp/models/nft_model.dart'; // Atualize o caminho conforme necessário
import 'package:myapp/services/blockchain_service.dart'; // Serviço para interações com o blockchain

class StoreScreen extends StatefulWidget {
  @override

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Store'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/home');
              },
              child: Text('Go to Home'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/store');
              },
              child: Text('Go to Store'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/login');
              },
              child: Text('Go to Login'),
            ),
          ],
        ),
      ),
    );
  }
}

class _StoreScreenState extends State<StoreScreen> {
  final TextEditingController _nftIdController = TextEditingController();
  final TextEditingController _nftNameController = TextEditingController();
  final TextEditingController _nftImageUrlController = TextEditingController();
  final TextEditingController _amountController = TextEditingController();

  Future<void> _mintNFT() async {
    String nftId = _nftIdController.text;
    String nftName = _nftNameController.text;
    String imageUrl = _nftImageUrlController.text;

    // Cunhar NFT com taxa "mynftcoin"
    try {
      await BlockchainService.mintNFT(nftId, nftName, imageUrl, 10); // 10 "mynftcoin" como taxa
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('NFT cunhado com sucesso')));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Erro ao cunhar NFT: $e')));
    }
  }

  Future<void> _swapMaticForMyCoin() async {
    double amount = double.parse(_amountController.text);

    // Trocar MATIC por "mycoin"
    try {
      await BlockchainService.swapMaticForMyCoin(amount);
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Troca de MATIC por mycoin realizada com sucesso')));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Erro ao trocar MATIC por mycoin: $e')));
    }
  }

  Future<void> _swapEthForMy() async {
    double amount = double.parse(_amountController.text);

    // Trocar ETH por "my"
    try {
      await BlockchainService.swapEthForMy(amount);
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Troca de ETH por my realizada com sucesso')));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Erro ao trocar ETH por my: $e')));
    }
  }

  Future<void> _stakeMyNFTCoin() async {
    double amount = double.parse(_amountController.text);

    // Staking de "mynftcoin"
    try {
      await BlockchainService.stakeMyNFTCoin(amount);
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Staking de mynftcoin realizado com sucesso')));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Erro ao realizar staking de mynftcoin: $e')));
    }
  }

  Future<void> _burnNFT() async {
    String nftId = _nftIdController.text;

    // Destruir NFT com taxa "mycoin"
    try {
      NFT nft = await BlockchainService.getNFT(nftId);
      await BlockchainService.burnNFT(nftId, 5); // 5 "mycoin" como taxa

      // Atualiza a raridade do NFT após destruição
      NFT updatedNFT = nft.withIncreasedRarity();
      await BlockchainService.updateNFTRarity(nftId, updatedNFT.rarity);

      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('NFT destruído com sucesso e raridade aumentada')));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Erro ao destruir NFT: $e')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Loja de NFTs'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ListView(
          children: [
            TextField(
              controller: _nftIdController,
              decoration: InputDecoration(labelText: 'ID do NFT'),
            ),
            TextField(
              controller: _nftNameController,
              decoration: InputDecoration(labelText: 'Nome do NFT'),
            ),
            TextField(
              controller: _nftImageUrlController,
              decoration: InputDecoration(labelText: 'URL da Imagem do NFT'),
            ),
            TextField(
              controller: _amountController,
              decoration: InputDecoration(labelText: 'Quantidade'),
              keyboardType: TextInputType.numberWithOptions(decimal: true),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _mintNFT,
              child: Text('Cunhar NFT'),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: _swapMaticForMyCoin,
              child: Text('Trocar MATIC por mycoin'),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: _swapEthForMy,
              child: Text('Trocar ETH por my'),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: _stakeMyNFTCoin,
              child: Text('Staking de mynftcoin'),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: _burnNFT,
              child: Text('Destruir NFT'),
            ),
          ],
        ),
      ),
    );
  }
}