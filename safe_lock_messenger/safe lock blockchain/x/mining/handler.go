package mining

import (
	"github.com/cosmos/cosmos-sdk/types"
	"safe lock blockchain/x/mceliece"
)

func handleMsgMine(ctx sdk.Context, msg types.MsgMine, k Keeper) sdk.Result {
	// Validate PoW difficulty
	difficulty := k.GetBlockDifficulty(ctx)
	if msg.Difficulty < difficulty {
		return sdk.ErrUnknownRequest("Invalid difficulty").Result()
	}

	// Validate proof of work
	m := mceliece.NewMcEliece(1024, 512, 128)
	hash, err := m.Hash(msg.Proof)
	if err != nil {
		return sdk.ErrUnknownRequest("Invalid proof of work").Result()
	}
	if !k.ValidateProofOfWork(ctx, hash, msg.Difficulty) {
		return sdk.ErrUnknownRequest("Invalid proof of work").Result()
	}

	// Calculate mining reward
	reward := k.GetMiningReward(ctx)

	// Emit mining event
	ctx.EventManager().EmitEvent(
		sdk.NewEvent(
			"mine",
			sdk.NewAttribute("miner", msg.Creator),
			sdk.NewAttribute("reward", reward.String()),
		),
	)

	// Update miner's account
	account := k.GetAccount(ctx, msg.Creator)
	account.SetCoins(account.GetCoins().Add(reward))
	k.SetAccount(ctx, account)

	return sdk.Result{Events: ctx.EventManager().Events()}
}

func (k Keeper) ValidateProofOfWork(ctx sdk.Context, hash []byte, difficulty int) bool {
	// Validate the proof of work using the McEliece algorithm
	m := mceliece.NewMcEliece(1024, 512, 128)
	return m.Verify(hash, difficulty)
}

func (k Keeper) GetBlockDifficulty(ctx sdk.Context) int {
	// Retrieve the current block difficulty from the store
	store := ctx.KVStore(k.storeKey)
	difficulty := store.Get(types.DifficultyKey())
	if difficulty == nil {
		return 1 // default difficulty
	}
	return int(difficulty.(uint64))
}

func (k Keeper) GetMiningReward(ctx sdk.Context) types.MiningReward {
	// Retrieve the current mining reward from the store
	store := ctx.KVStore(k.storeKey)
	reward := store.Get(types.RewardKey())
	if reward == nil {
		return types.MiningReward{Amount: sdk.NewInt(10)} // default reward
	}
	return reward.(types.MiningReward)
}