import (
    sdk "github.com/cosmos/cosmos-sdk/types"
)

const (
    TypeMsgMint = "mint"
    TypeMsgBurn = "burn"
)

type MsgMint struct {
    Id       string `json:"id"`
    Name     string `json:"name"`
    ImageUrl string `json:"image_url"`
    Fee      int64  `json:"fee"`
    Creator  sdk.AccAddress `json:"creator"`
}

func NewMsgMint(id, name, imageUrl string, fee int64, creator sdk.AccAddress) MsgMint {
    return MsgMint{
        Id:       id,
        Name:     name,
        ImageUrl: imageUrl,
        Fee:      fee,
        Creator:  creator,
    }
}

func (msg MsgMint) Route() string { return RouterKey }
func (msg MsgMint) Type() string  { return TypeMsgMint }
func (msg MsgMint) ValidateBasic() error {
    if msg.Id == "" || msg.Name == "" || msg.Creator.Empty() {
        return sdk.ErrInvalidAddress(msg.Creator.String())
    }
    return nil
}

type MsgBurn struct {
    Id       string `json:"id"`
    Fee      int64  `json:"fee"`
    Creator  sdk.AccAddress `json:"creator"`
}

func NewMsgBurn(id string, fee int64, creator sdk.AccAddress) MsgBurn {
    return MsgBurn{
        Id:       id,
        Fee:      fee,
        Creator:  creator,
    }
}

func (msg MsgBurn) Route() string { return RouterKey }
func (msg MsgBurn) Type() string  { return TypeMsgBurn }
func (msg MsgBurn) ValidateBasic() error {
    if msg.Id == "" || msg.Creator.Empty() {
        return sdk.ErrInvalidAddress(msg.Creator.String())
    }
    return nil
}