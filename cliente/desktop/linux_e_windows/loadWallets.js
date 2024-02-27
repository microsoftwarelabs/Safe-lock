function loadWalletsFromFile() {
    fetch('wallets.txt')
        .then(response => response.text())
        .then(contents => {
            const wallets = contents.split('\n').map(wallet => wallet.trim());
            console.log('Carteiras carregadas:', wallets);
            // Aqui você pode fazer o que quiser com as carteiras carregadas
        })
        .catch(error => console.error('Erro ao carregar o arquivo:', error));
}