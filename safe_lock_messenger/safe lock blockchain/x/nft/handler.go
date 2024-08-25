import (
    sdk "github.com/cosmos/cosmos-sdk/types"
    "github.com/myorg/mychain/x/nft/types"
)

func handleMsgMint(ctx sdk.Context, k Keeper, msg types.MsgMint) sdk.Result {
    nft := types.NewNFT(msg.Id, msg.Name, msg.ImageUrl, 0)

    // Deduz taxa de "mynftcoin"
    fee := sdk.NewCoin("mynftcoin", sdk.NewInt(msg.Fee))
    account := k.accountKeeper.GetAccount(ctx, msg.Creator)
    if !account.GetCoins().IsAllGTE(sdk.Coins{fee}) {
        return sdk.ErrInsufficientFunds("Insufficient funds for minting NFT").Result()
    }

    account.SetCoins(account.GetCoins().Sub(fee))
    k.accountKeeper.SetAccount(ctx, account)

    // Cunha o NFT
    k.SetNFT(ctx, nft)

    return sdk.Result{}
}

func handleMsgBurn(ctx sdk.Context, k Keeper, msg types.MsgBurn) sdk.Result {
    nft, found := k.GetNFT(ctx, msg.Id)
    if !found {
        return sdk.ErrUnknownRequest("NFT not found").Result()
    }

    // Deduz taxa de "mycoin"
    fee := sdk.NewCoin("mycoin", sdk.NewInt(msg.Fee))
    account := k.accountKeeper.GetAccount(ctx, msg.Creator)
    if !account.GetCoins().IsAllGTE(sdk.Coins{fee}) {
        return sdk.ErrInsufficientFunds("Insufficient funds for burning NFT").Result()
    }

    account.SetCoins(account.GetCoins().Sub(fee))
    k.accountKeeper.SetAccount(ctx, account)

    // Deleta o NFT e aumenta a raridade
    k.DeleteNFT(ctx, msg.Id)
    err := k.IncreaseRarity(ctx, msg.Id)
    if err != nil {
        return err.Result()
    }

    return sdk.Result{}
}