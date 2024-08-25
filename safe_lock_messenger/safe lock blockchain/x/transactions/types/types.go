import (
    sdk "github.com/cosmos/cosmos-sdk/types"
)

const (
    ModuleName = "transactions"
    StoreKey   = ModuleName
)

type MsgDeposit struct {
    Creator string
    Amount   int64
}

type MsgWithdraw struct {
    Creator string
    Amount   int64
}

func (msg MsgDeposit) Route() string { return ModuleName }
func (msg MsgDeposit) Type() string  { return "deposit" }

func (msg MsgWithdraw) Route() string { return ModuleName }
func (msg MsgWithdraw) Type() string  { return "withdraw" }