from web3 import Web3
import time
# Verbindungsdaten zu deiner Geth-Node
node_url = "http://127.0.0.1:9001"  # Update this to match your node's URL

# Verbindung zur Geth-Node herstellen
web3 = Web3(Web3.HTTPProvider(node_url))

# Überprüfen, ob die Verbindung erfolgreich ist

if web3.is_connected():
    print("Erfolgreich mit der Geth-Node verbunden")
else:
    print("Fehler bei der Verbindung zur Geth-Node")

# Konten abrufen
accounts = web3.eth.accounts
print("Konten:", accounts)

block_100 = web3.eth.get_block(100)
block_100_id = block_100['hash'].hex()
print(f"Block 100 ID: {block_100_id}")


# Adressen und private Schlüssel der Wallets (Beispieladressen)
source_address = "0x30DBFde92c0d62584597094C436FC241278DbbDc"
target_address = "0x3b5A5B160EeaD4918bd2D132aBf8665d019F861D"
private_key = "da5718ac70daadfe1faf1e55d27dbebc917e7f88430b6b892f967712c029802a"

calculated_address = web3.eth.account.from_key(private_key).address

if calculated_address.lower() != source_address.lower():
    print(f"Fehler: Die berechnete Adresse {calculated_address} stimmt nicht mit der angegebenen Quelladresse {source_address} überein.")
    exit()
print(f"Berechnete Adresse aus dem privaten Schlüssel: {calculated_address}")
# Betrag für jede Transaktion (in Wei)
balance = web3.eth.get_balance(source_address)
print(f"Kontostand von {source_address}: {web3.from_wei(balance, 'ether')} Ether")

amount = web3.to_wei(0.01, 'ether')  # Beispiel: 0.01 Ether pro Transaktion

# # Gaspreis und Gaslimit festlegen
gas_price = web3.to_wei(1, 'gwei')  # Beispiel: 50 Gwei
gas_limit = 21000  # Standard für einfache ETH-Transaktionen
chain_id = 15

def send_transaction(nonce):
    tx = {
        'nonce': nonce,
        'to': target_address,
        'value': amount,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'chainId': chain_id
    }

    print(f"Erstellen der Transaktion: {tx}")
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    print(f"Signierte Transaktion: {signed_tx.rawTransaction.hex()}")
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash

# Senden von 1000 Transaktionen
nonce = web3.eth.get_transaction_count(source_address)
for i in range(1000):
    tx_hash = send_transaction(nonce + i)
    print(f'Transaktion {i+1}/1000 gesendet, TX Hash: {tx_hash.hex()}')
    # Optional: kleine Pause zwischen den Transaktionen
    time.sleep(0.1)

print("1000 Transaktionen erfolgreich gesendet")
# Mining starten
# if len(accounts) > 0:
#     miner_address = accounts[0]
#     web3.geth.miner.set_etherbase(miner_address)
#     web3.geth.miner.start(1)
#     print(f"Mining gestartet mit Etherbase: {miner_address}")
# else:
#     print("Keine Konten gefunden. Bitte erstelle oder importiere ein Konto in Geth.")
