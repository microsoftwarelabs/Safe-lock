import (
    sdk "github.com/cosmos/cosmos-sdk/types"
    "safe lock blockchain/x/transactions/types"
)

func handleMsgDeposit(ctx sdk.Context, msg types.MsgDeposit, k Keeper) sdk.Result {
    account := k.GetAccount(ctx, msg.Creator)
    deposit := sdk.NewCoin("mycoin", sdk.NewInt(msg.Amount))
    
    if !account.GetCoins().IsAllGTE(sdk.Coins{deposit}) {
        return sdk.ErrInsufficientFunds("Insufficient funds for deposit").Result()
    }

    account.SetCoins(account.GetCoins().Add(deposit))
    k.SetAccount(ctx, account)

    ctx.EventManager().EmitEvent(
        sdk.NewEvent(
            types.EventTypeDeposit,
            sdk.NewAttribute(types.AttributeKeyDepositor, msg.Creator),
            sdk.NewAttribute(types.AttributeKeyAmount, deposit.String()),
        ),
    )

    return sdk.Result{}
}

func handleMsgWithdraw(ctx sdk.Context, msg types.MsgWithdraw, k Keeper) sdk.Result {
    account := k.GetAccount(ctx, msg.Creator)
    withdrawal := sdk.NewCoin("mycoin", sdk.NewInt(msg.Amount))
    
    if !account.GetCoins().IsAllGTE(sdk.Coins{withdrawal}) {
        return sdk.ErrInsufficientFunds("Insufficient funds for withdrawal").Result()
    }
    
    if !account.GetCoins().IsAllGTE(sdk.Coins{
        sdk.NewCoin("mycoin", sdk.NewInt(10)), // Example withdrawal fee
        sdk.NewCoin("mynftcoin", sdk.NewInt(1)), // Example condition
    }) {
        return sdk.ErrInsufficientFunds("Insufficient mycoin or mynftcoin for withdrawal").Result()
    }
    
    account.SetCoins(account.GetCoins().Sub(withdrawal))
    k.SetAccount(ctx, account)
    
    fee := sdk.NewCoin("mycoin", sdk.NewInt(2))
    account.SetCoins(account.GetCoins().Sub(fee))
    k.SetAccount(ctx, account)
    
    ctx.EventManager().EmitEvent(
        sdk.NewEvent(
            types.EventTypeWithdraw,
            sdk.NewAttribute(types.AttributeKeyWithdrawer, msg.Creator),
            sdk.NewAttribute(types.AttributeKeyAmount, withdrawal.String()),
        ),
    )
    
    return sdk.Result{}
}