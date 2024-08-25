package app

import (
	"safe lock blockchain/x/nft"
	"safe lock blockchain/x/token_swap"
	"safe lock blockchain/x/staking"
	"github.com/CosmWasm/wasmd/x/wasm"
	"github.com/cosmos/cosmos-sdk/codec"
	"github.com/cosmos/cosmos-sdk/x/auth"
	"github.com/cosmos/cosmos-sdk/x/bank"
	sdk "github.com/cosmos/cosmos-sdk/types"
	baseapp "github.com/cosmos/cosmos-sdk/baseapp"
	abci "github.com/tendermint/tendermint/abci/types"
	"github.com/cosmos/cosmos-sdk/store"
)

type App struct {
	*baseapp.BaseApp
	cdc             *codec.Codec
	keyNFT          *sdk.KVStoreKey
	nftKeeper       nft.Keeper
	keyTokenSwap    *sdk.KVStoreKey
	tokenSwapKeeper token_swap.Keeper
	keyStaking      *sdk.KVStoreKey
	stakingKeeper   staking.Keeper
	keyWasm         *sdk.KVStoreKey
	wasmKeeper      wasm.Keeper
}

// Nova instância de App com o módulo CosmWasm
func NewApp(logger log.Logger, db db.DB) *App {
	cdc := codec.NewLegacyAmino()
	keyMain := sdk.NewKVStoreKey("main")
	keyWasm := sdk.NewKVStoreKey(wasm.StoreKey)
	keyNFT := sdk.NewKVStoreKey(nft.ModuleName)
	keyTokenSwap := sdk.NewKVStoreKey(token_swap.ModuleName)
	keyStaking := sdk.NewKVStoreKey(staking.ModuleName)

	app := baseapp.NewBaseApp("mychain", logger, db, cdc)

	// Criar Keepers
	nftKeeper := nft.NewKeeper(cdc, keyNFT)
	tokenSwapKeeper := token_swap.NewKeeper(cdc, keyTokenSwap)
	stakingKeeper := staking.NewKeeper(cdc, keyStaking)
	wasmKeeper := wasm.NewKeeper(
		cdc,
		keyWasm,
		wasm.DefaultGasLimit,   // Limite de gás padrão
		wasm.DefaultMaxContractSize, // Tamanho máximo de contrato
	)

	// Configurar o BaseApp e adicionar módulos
	app.Router().
		AddRoute(nft.ModuleName, nft.NewHandler(nftKeeper)).
		AddRoute(token_swap.ModuleName, token_swap.NewHandler(tokenSwapKeeper)).
		AddRoute(staking.ModuleName, staking.NewHandler(stakingKeeper)).
		AddRoute(wasm.ModuleName, wasm.NewHandler(wasmKeeper))

	app.SetInitChainer(func(ctx sdk.Context, req abci.RequestInitChain) abci.ResponseInitChain {
		// Inicialize o estado do aplicativo se necessário
		return abci.ResponseInitChain{}
	})

	app.SetEndBlocker(func(ctx sdk.Context, req abci.RequestEndBlock) abci.ResponseEndBlock {
		// Finalize o bloco e faça o processamento final
		return abci.ResponseEndBlock{}
	})

	app.SetAnteHandler(auth.NewAnteHandler(auth.NewAccountKeeper(cdc, keyMain), auth.NewBankKeeper(cdc, keyMain)))

	// Configuração de store
	app.MountStores(keyMain, keyWasm, keyNFT, keyTokenSwap, keyStaking)

	return &App{
		BaseApp:         app,
		cdc:             cdc,
		keyNFT:          keyNFT,
		nftKeeper:       nftKeeper,
		keyTokenSwap:    keyTokenSwap,
		tokenSwapKeeper: tokenSwapKeeper,
		keyStaking:      keyStaking,
		stakingKeeper:   stakingKeeper,
		keyWasm:         keyWasm,
		wasmKeeper:      wasmKeeper,
	}
}