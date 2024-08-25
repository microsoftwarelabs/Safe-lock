import 'package:http/http.dart' as http;
import 'dart:convert';

class BlockchainService {
  static const String baseUrl = 'https://your-blockchain-api-url.com';

  // Função para cunhar NFTs
  static Future<void> mintNFT(String id, String name, String imageUrl, int fee) async {
    final response = await http.post(
      Uri.parse('$baseUrl/mint_nft'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'id': id,
        'name': name,
        'imageUrl': imageUrl,
        'fee': fee,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception('Falha ao cunhar NFT');
    }
  }

  // Função para trocar MATIC por mycoin
  static Future<void> swapMaticForMyCoin(double amount) async {
    final response = await http.post(
      Uri.parse('$baseUrl/swap_matic_for_mycoin'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'amount': amount}),
    );

    if (response.statusCode != 200) {
      throw Exception('Falha ao trocar MATIC por mycoin');
    }
  }

  // Função para trocar ETH por my
  static Future<void> swapEthForMy(double amount) async {
    final response = await http.post(
      Uri.parse('$baseUrl/swap_eth_for_my'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'amount': amount}),
    );

    if (response.statusCode != 200) {
      throw Exception('Falha ao trocar ETH por my');
    }
  }

  // Função para staking de myNFTcoin
  static Future<void> stakeMyNFTCoin(double amount) async {
    final response = await http.post(
      Uri.parse('$baseUrl/stake_mynftcoin'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'amount': amount}),
    );

    if (response.statusCode != 200) {
      throw Exception('Falha ao realizar staking de mynftcoin');
    }
  }

  // Função para obter informações do NFT
  static Future<NFT> getNFT(String id) async {
    final response = await http.get(Uri.parse('$baseUrl/nft/$id'));

    if (response.statusCode != 200) {
      throw Exception('Falha ao obter NFT');
    }

    final data = json.decode(response.body);
    return NFT(
      id: data['id'],
      name: data['name'],
      imageUrl: data['imageUrl'],
      rarity: data['rarity'],
    );
  }

  // Função para destruir NFT
  static Future<void> burnNFT(String id, int fee) async {
    final response = await http.post(
      Uri.parse('$baseUrl/burn_nft'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'id': id,
        'fee': fee,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception('Falha ao destruir NFT');
    }
  }

  // Função para atualizar a raridade do NFT
  static Future<void> updateNFTRarity(String id, int rarity) async {
    final response = await http.put(
      Uri.parse('$baseUrl/update_nft_rarity'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'id': id,
        'rarity': rarity,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception('Falha ao atualizar raridade do NFT');
    }
  }
}