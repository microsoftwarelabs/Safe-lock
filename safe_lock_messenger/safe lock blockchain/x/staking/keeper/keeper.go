import (
    sdk "github.com/cosmos/cosmos-sdk/types"
    "github.com/myorg/mychain/x/staking/types"
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

func (k Keeper) StakeMyNFTCoin(ctx sdk.Context, amount sdk.Int) error {
    // Verificar se o usuário tem saldo suficiente
    if !k.HasBalance(ctx, ctx.FromAddress(), amount) {
        return sdkerrors.Wrap(sdkerrors.ErrInsufficientFunds, "saldo insuficiente")
    }

    // Debitar o saldo do usuário
    k.SubtractBalance(ctx, ctx.FromAddress(), amount)

    // Adicionar o staking ao store
    store := ctx.KVStore(k.storeKey)
    store.Set(types.StakingKey(ctx.FromAddress()), amount)

    return nil
}

func (k Keeper) UnstakeMyNFTCoin(ctx sdk.Context, amount sdk.Int) error {
    // Verificar se o usuário tem staking suficiente
    if !k.HasStaking(ctx, ctx.FromAddress(), amount) {
        return sdkerrors.Wrap(sdkerrors.ErrInvalidRequest, "staking insuficiente")
    }

    // Remover o staking do store
    store := ctx.KVStore(k.storeKey)
    store.Delete(types.StakingKey(ctx.FromAddress()))

    // Creditar o saldo do usuário
    k.AddBalance(ctx, ctx.FromAddress(), amount)

    return nil
}

func (k Keeper) DelegateMyNFTCoin(ctx sdk.Context, delegator sdk.AccAddress, validator sdk.ValAddress, amount sdk.Int) error {
    // Verificar se o usuário tem staking suficiente
    if !k.HasStaking(ctx, delegator, amount) {
        return sdkerrors.Wrap(sdkerrors.ErrInvalidRequest, "staking insuficiente")
    }

    // Verificar se o validador é válido
    if !k.IsValidator(ctx, validator) {
        return sdkerrors.Wrap(sdkerrors.ErrInvalidRequest, "validador inválido")
    }

    // Debitar o staking do usuário
    k.SubtractStaking(ctx, delegator, amount)

    // Adicionar o staking ao validador
    k.AddValidatorStaking(ctx, validator, amount)

    return nil
}

func (k Keeper) RewardMyNFTCoin(ctx sdk.Context, validator sdk.ValAddress, amount sdk.Int) error {
    // Verificar se o validador é válido
    if !k.IsValidator(ctx, validator) {
        return sdkerrors.Wrap(sdkerrors.ErrInvalidRequest, "validador inválido")
    }

    // Adicionar o reward ao validador
    k.AddValidatorReward(ctx, validator, amount)

    return nil
}