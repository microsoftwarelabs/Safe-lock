class NFT {
  final String id;
  final String name;
  final String imageUrl;
  final int rarity;

  NFT({
    required this.id,
    required this.name,
    required this.imageUrl,
    required this.rarity,
  });

  // Atualiza a raridade do NFT
  NFT withIncreasedRarity() {
    return NFT(
      id: id,
      name: name,
      imageUrl: imageUrl,
      rarity: rarity + 1,
    );
  }
}