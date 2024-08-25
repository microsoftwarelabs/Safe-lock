import (
    sdk "github.com/cosmos/cosmos-sdk/types"
    "github.com/myorg/mychain/x/token_swap/types"
)

func handleMsgSwapMaticForMyCoin(ctx sdk.Context, k Keeper, msg types.MsgSwapMaticForMyCoin) sdk.Result {
    err := k.SwapMaticForMyCoin(ctx, msg.Amount)
    if err != nil {
        return err.Result()
    }

    return sdk.Result{}
}

func handleMsgSwapEthForMy(ctx sdk.Context, k Keeper, msg types.MsgSwapEthForMy) sdk.Result {
    err := k.SwapEthForMy(ctx, msg.Amount)
    if err != nil {
        return err.Result()
    }

    return sdk.Result{}
}