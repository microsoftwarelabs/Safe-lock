import (
    sdk "github.com/cosmos/cosmos-sdk/types"
)

const (
    ModuleName = "mining"
    StoreKey   = ModuleName
)

type MsgMine struct {
    Creator string
    Difficulty int // PoW difficulty level
    Proof     string // Proof of work
}

func (msg MsgMine) Route() string { return ModuleName }
func (msg MsgMine) Type() string  { return "mine" }

type MiningReward struct {
    Amount sdk.Int
}

func (reward MiningReward) String() string {
    return reward.Amount.String()
}