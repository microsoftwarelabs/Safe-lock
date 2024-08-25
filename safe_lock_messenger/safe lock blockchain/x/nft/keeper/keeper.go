import (
    sdk "github.com/cosmos/cosmos-sdk/types"
    "github.com/myorg/mychain/x/nft/types"
)

type Keeper struct {
    storeKey sdk.StoreKey
    cdc      *codec.Codec
}

func NewKeeper(cdc *codec.Codec, storeKey sdk.StoreKey) Keeper {
    return Keeper{
        storeKey: storeKey,
        cdc:      cdc,
    }
}

func (k Keeper) GetNFT(ctx sdk.Context, id string) (types.NFT, bool) {
    store := ctx.KVStore(k.storeKey)
    bytes := store.Get([]byte(id))
    if bytes == nil {
        return types.NFT{}, false
    }

    var nft types.NFT
    k.cdc.MustUnmarshalBinaryBare(bytes, &nft)
    return nft, true
}

func (k Keeper) SetNFT(ctx sdk.Context, nft types.NFT) {
    store := ctx.KVStore(k.storeKey)
    store.Set([]byte(nft.Id), k.cdc.MustMarshalBinaryBare(&nft))
}

func (k Keeper) DeleteNFT(ctx sdk.Context, id string) {
    store := ctx.KVStore(k.storeKey)
    store.Delete([]byte(id))
}

func (k Keeper) IncreaseRarity(ctx sdk.Context, id string) error {
    nft, found := k.GetNFT(ctx, id)
    if !found {
        return sdk.ErrUnknownRequest("NFT not found")
    }

    nft.Rarity += 1
    k.SetNFT(ctx, nft)
    return nil
}