import (
    sdk "github.com/cosmos/cosmos-sdk/types"
)

const (
    TypeMsgSwapMaticForMyCoin = "swap_matic_for_mycoin"
    TypeMsgSwapEthForMy       = "swap_eth_for_my"
)

type MsgSwapMaticForMyCoin struct {
    Amount sdk.Int `json:"amount"`
    Creator sdk.AccAddress `json:"creator"`
}

func NewMsgSwapMaticForMyCoin(amount sdk.Int, creator sdk.AccAddress) MsgSwapMaticForMyCoin {
    return MsgSwapMaticForMyCoin{
        Amount: amount,
        Creator: creator,
    }
}

func (msg MsgSwapMaticForMyCoin) Route() string { return RouterKey }
func (msg MsgSwapMaticForMyCoin) Type() string  { return TypeMsgSwapMaticForMyCoin }
func (msg MsgSwapMaticForMyCoin) ValidateBasic() error {
    if msg.Amount.IsNegative() || msg.Creator.Empty() {
        return sdk.ErrInvalidAddress(msg.Creator.String())
    }
    return nil
}

type MsgSwapEthForMy struct {
    Amount sdk.Int `json:"amount"`
    Creator sdk.AccAddress `json:"creator"`
}

func NewMsgSwapEthForMy(amount sdk.Int, creator sdk.AccAddress) MsgSwapEthForMy {
    return MsgSwapEthForMy{
        Amount: amount,
        Creator: creator,
    }
}

func (msg MsgSwapEthForMy) Route() string { return RouterKey }
func (msg MsgSwapEthForMy) Type() string  { return TypeMsgSwapEthForMy }
func (msg MsgSwapEthForMy) ValidateBasic() error {
    if msg.Amount.IsNegative() || msg.Creator.Empty() {
        return sdk.ErrInvalidAddress(msg.Creator.String())
    }
    return nil
}