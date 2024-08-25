package mceliece

import (
	"crypto/rand"
	"encoding/binary"
	"errors"
	"fmt"
	"math/big"
)

// McEliece é a estrutura que representa o algoritmo McEliece
type McEliece struct {
	n, k, t int
	G       [][]byte
	P       [][]byte
	S       []byte
}

// NewMcEliece retorna uma nova instância do algoritmo McEliece
func NewMcEliece(n, k, t int) (*McEliece, error) {
	if n < k || k < t || t < 1 {
		return nil, errors.New("invalid parameters")
	}
	m := &McEliece{n: n, k: k, t: t}
	m.G = make([][]byte, k)
	m.P = make([][]byte, k)
	m.S = make([]byte, n-k)
	for i := 0; i < k; i++ {
		m.G[i] = make([]byte, n)
		m.P[i] = make([]byte, k)
	}
	return m, nil
}

// GenerateKey gera uma chave pública e privada para o algoritmo McEliece
func (m *McEliece) GenerateKey() ([]byte, []byte, error) {
	pubKey := make([]byte, m.n*m.k)
	privKey := make([]byte, m.k*m.k)
	for i := 0; i < m.k; i++ {
		for j := 0; j < m.n; j++ {
			pubKey[i*m.n+j] = byte(rand.Intn(2))
		}
		for j := 0; j < m.k; j++ {
			privKey[i*m.k+j] = byte(rand.Intn(2))
		}
	}
	return pubKey, privKey, nil
}

// Encrypt encrypta um mensagem usando a chave pública
func (m *McEliece) Encrypt(pubKey []byte, msg []byte) ([]byte, error) {
	if len(msg) != m.k {
		return nil, errors.New("invalid message length")
	}
	ciphertext := make([]byte, m.n)
	for i := 0; i < m.n; i++ {
		c := byte(0)
		for j := 0; j < m.k; j++ {
			c ^= pubKey[i*m.k+j] & msg[j]
		}
		ciphertext[i] = c
	}
	return ciphertext, nil
}

// Decrypt decrypta um ciphertext usando a chave privada
func (m *McEliece) Decrypt(privKey []byte, ciphertext []byte) ([]byte, error) {
	if len(ciphertext) != m.n {
		return nil, errors.New("invalid ciphertext length")
	}
	msg := make([]byte, m.k)
	for i := 0; i < m.k; i++ {
		m := byte(0)
		for j := 0; j < m.n; j++ {
			m ^= privKey[i*m.k+j] & ciphertext[j]
		}
		msg[i] = m
	}
	return msg, nil
}

// Hash calcula o hash da prova de trabalho usando o algoritmo McEliece
func (m *McEliece) Hash(proof []byte) ([]byte, error) {
	pubKey, _, err := m.GenerateKey()
	if err != nil {
		return nil, err
	}
	ciphertext, err := m.Encrypt(pubKey, proof)
	if err != nil {
		return nil, err
	}
	hash := make([]byte, m.n)
	for i := 0; i < m.n; i++ {
		hash[i] = ciphertext[i]
	}
	return hash, nil
}