import (
    sdk "github.com/cosmos/cosmos-sdk/types"
    "github.com/myorg/mychain/x/staking/types"
)

func handleMsgStakeMyNFTCoin(ctx sdk.Context, k Keeper, msg types.MsgStakeMyNFTCoin) sdk.Result {
    err := k.StakeMyNFTCoin(ctx, msg.Amount)
    if err != nil {
        return err.Result()
    }

    return sdk.Result{}
}

func handleMsgUnstakeMyNFTCoin(ctx sdk.Context, k Keeper, msg types.MsgUnstakeMyNFTCoin) sdk.Result {
    err := k.UnstakeMyNFTCoin(ctx, msg.Amount)
    if err != nil {
        return err.Result()
    }

    return sdk.Result{}
}

func handleMsgDelegateMyNFTCoin(ctx sdk.Context, k Keeper, msg types.MsgDelegateMyNFTCoin) sdk.Result {
    err := k.DelegateMyNFTCoin(ctx, msg.Delegator, msg.Validator, msg.Amount)
    if err != nil {
        return err.Result()
    }

    return sdk.Result{}
}

func handleMsgRewardMyNFTCoin(ctx sdk.Context, k Keeper, msg types.MsgRewardMyNFTCoin) sdk.Result {
    err := k.RewardMyNFTCoin(ctx, msg.Validator, msg.Amount)
    if err != nil {
        return err.Result()
    }

    return sdk.Result{}
}