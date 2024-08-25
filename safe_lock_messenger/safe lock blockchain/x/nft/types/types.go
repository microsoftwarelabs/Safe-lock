import (
    sdk "github.com/cosmos/cosmos-sdk/types"
)

type NFT struct {
    Id       string         `json:"id"`
    Name     string         `json:"name"`
    ImageUrl string         `json:"image_url"`
    Rarity   int            `json:"rarity"`
}

func NewNFT(id, name, imageUrl string, rarity int) NFT {
    return NFT{
        Id:       id,
        Name:     name,
        ImageUrl: imageUrl,
        Rarity:   rarity,
    }
}

func (nft NFT) Validate() error {
    if nft.Id == "" || nft.Name == "" {
        return sdk.ErrUnknownRequest("NFT ID and Name cannot be empty")
    }
    return nil
}