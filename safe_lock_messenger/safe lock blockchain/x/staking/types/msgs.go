import (
    sdk "github.com/cosmos/cosmos-sdk/types"
)

const (
    TypeMsgStakeMyNFTCoin = "stake_mynftcoin"
)

type MsgStakeMyNFTCoin struct {
    Amount sdk.Int `json:"amount"`
    Staker sdk.AccAddress `json:"staker"`
}

func NewMsgStakeMyNFTCoin(amount sdk.Int, staker sdk.AccAddress) MsgStakeMyNFTCoin {
    return MsgStakeMyNFTCoin{
        Amount: amount,
        Staker: staker,
    }
}

func (msg MsgStakeMyNFTCoin) Route() string { return RouterKey }
func (msg MsgStakeMyNFTCoin) Type() string  { return TypeMsgStakeMyNFTCoin }
func (msg MsgStakeMyNFTCoin) ValidateBasic() error {
    if msg.Amount.IsNegative() || msg.Staker.Empty() {
        return sdk.ErrInvalidAddress(msg.Staker.String())
    }
    return nil
}