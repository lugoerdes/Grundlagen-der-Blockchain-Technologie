from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Verbindung zur Bitcoin-Node
rpc_user = 'kuhmist123'
rpc_password = 'kuhmist1234'
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:18443")

# Token-Parameter
name = "TestToken"
symbol = "TTK"
total_supply = 1000000
decimals = 8
address = rpc_connection.getnewaddress()

# Beispiel-Token-Transaktion (für echte Implementierung erweiterbar)
txid = rpc_connection.sendtoaddress(address, 0.01, "Create Token", f"{name}|{symbol}|{total_supply}|{decimals}")

print(f"Token erstellt mit Transaktions-ID: {txid}")
print(f"Token Name: {name}")
print(f"Token Symbol: {symbol}")
print(f"Total Supply: {total_supply}")
print(f"Decimals: {decimals}")
print(f"Token-Adresse: {address}")
