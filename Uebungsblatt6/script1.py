from web3 import Web3
import time
from eth_account.messages import encode_defunct
from eth_account import Account
import json

# Verbindung zur lokalen Geth-Node herstellen
node_url = "http://127.0.0.1:9001"
web3 = Web3(Web3.HTTPProvider(node_url, request_kwargs={'timeout': 60}))

# Überprüfen, ob die Verbindung erfolgreich ist
if not web3.is_connected():
    print("Fehler bei der Verbindung zur Geth-Node")
    exit()

def sixC():
    max_tx_block = None
    max_tx_count = 0

    # Aktuelle Blocknummer abrufen
    latest_block = web3.eth.block_number
    print(f"Neuester Block: {latest_block}")

    # Durchsuche alle Blöcke von 0 bis zum neuesten Block
    for block_number in range(latest_block + 1):
        block = web3.eth.get_block(block_number)
        tx_count = len(block.transactions)

        if tx_count > max_tx_count:
            max_tx_block = block_number
            max_tx_count = tx_count

    print(f"Der Block mit den meisten Transaktionen ist Block {max_tx_block} mit {max_tx_count} Transaktionen.")
# sixC()
def sixD():
    # Adressen und private Schlüssel der Wallets
    source_address = "0x30DBFde92c0d62584597094C436FC241278DbbDc"
    private_key = "da5718ac70daadfe1faf1e55d27dbebc917e7f88430b6b892f967712c029802a"

    # PGP Public Key als Daten
    pgp_public_key = """-----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: Keybase OpenPGP v1.0.0
    Comment: https://keybase.io/crypto

    xo0EZn1JlQEEAL0k9Op+qBTq5TWMMfX5ngCRONs4rqQqzxCdzfpj5Av/TM7vaGHq
    gllWfbpXqmM6ydjt5rUc1vE64+8nLjx4SqcqFZOUEvrFKtQdU2bDMU20eDosMO3D
    bsX/OVkvP7EjrC/RGyKvly52IyD8tnoJ4ZceNY3Hlh208Tvxxfi2PyADABEBAAHN
    IUx1aXMgKFRlc3QpIDxsdWdvZXJkZXNAZ21haWwuY29tPsKtBBMBCgAXBQJmfUmV
    AhsvAwsJBwMVCggCHgECF4AACgkQXUf8kpI75mKulwQAmJZXE1WBpVTs0NTl1BWh
    qchDAx41ikzm72fvHfsb54OEnPT3fBU2pohf0z7t8wFJlNVa0FCCRx43m1GMnpdq
    gcjOiVl0sTM4i68jn1W8cS3H57BaL2469ClUw7TIlVPrFTPvA7FhqaqanDsfSilR
    FIVfg0Zq4gbU60AmWPQIQYnOjQRmfUmVAQQA0fxaV5f/Mmv7Jz8JBopLe9WxfBMq
    gGtvY2uyjzeJzzooZf18YAuN/17kWiWDg4ZLocNqkX4Zlchk0fIoOnBwhMY+cktP
    T4zuYWGCFTtVWhKGzqcCJTl5rP+2Cz5pLm+EpQS+2DxXCSaZguwkk7FbxNu66Hy8
    zKMIHl5d0JcLg1UAEQEAAcLAgwQYAQoADwUCZn1JlQUJDwmcAAIbLgCoCRBdR/yS
    kjvmYp0gBBkBCgAGBQJmfUmVAAoJEJUcPLJW7UI5t9ED/A4sx0Rdp5V9XIFkdI5S
    szPFTsfEVP7bYmAQCh+5wZPveUpmvMEuYpjDK4CtLqknv1nPfKgxBPlHf6JJyZkg
    S40//En3VbKqll4pJSRekHCXdSQrqWh4aD3bdJFhvf+gC3st6VM0WXKm32ga2Bp4
    ISS9RTxIl3di3B0504KgiSrNXGgD/iAlZ2pEmM1QBuLn/TmqGUdVYBr4pxbE1CCm
    ZZfQylsKJwizJd6G8rSTxNIbchPttW9pmpGKjvgShlT2E9yae2kKcoij0oItVEB+
    hGZY3+NpfPXNNFi+9+MOXHx0vcAjHr0+OPn8DN+rtnJX2QMjP7W751LdGmx3VhgJ
    edAxJfMOzo0EZn1JlQEEAMAq7pXcuxq960kEf9w1zaiA+HIRa8MBdx/4jNipViMw
    K2vHZLeH9I6kE+669t3ROT1G1Mv+RzAjxNydix4+M7hrapTxqX624mpy7Kxp7mN7
    aaCFyQ6ZZpA+4RNE3atfZGo7jB99KHdziepYIlEcKdQTZP7agH3zVme1zmWJeD2b
    ABEBAAHCwIMEGAEKAA8FAmZ9SZUFCQ8JnAACGy4AqAkQXUf8kpI75mKdIAQZAQoA
    BgUCZn1JlQAKCRC+dHiydyL56kzgBACoYfZ4nOXPmVctg/ZCCvZXdxevf/jG7+GF
    DVQReSDDX88QZXV9Am6pTeFCZULCh4b8V8QzJnqRTE1YJjFK2QfTLoXI2bxRXClr
    748y49JVy6PwTfaJ4SnpmkPRr9vAvYUjubG8fzPTa6Wl2xRB/OhgQQ6kcuznfADJ
    IpRcADjerRXpA/9S7m+8k0uredmv7gsp6Z2DFqSO+p/iRazbShOcs144VnziPPR4
    1846FbDe77vZMs6sTVzwLFgYZkx8l7sWkyVtSPEV2ScKljIPLTCC6cfEWwGnp198
    tkrOpbSKvgEaClsCePsfVFQ5zI7K7eDNMy0gBHgApka3DxyVvcSoRgvOwA==
    =F4E+
    -----END PGP PUBLIC KEY BLOCK-----"""

    # Nonce für die Transaktion abrufen
    nonce = web3.eth.get_transaction_count(source_address)

    # Betrag und Gaslimit festlegen (hier wird kein Ether übertragen, nur Daten)
    amount = 0
    gas_limit = 300000  # Erhöhtes Gaslimit, da die Datenmenge groß ist
    gas_price = web3.to_wei(50, 'gwei')

    # Erstellen der Transaktion
    tx = {
        'nonce': nonce,
        'to': source_address,  # Die Transaktion wird an dich selbst gesendet
        'value': amount,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'data': Web3.to_hex(text=pgp_public_key),
        'chainId': 108
    }

    # Signieren der Transaktion
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    print(f"Signierte Transaktion: {signed_tx.rawTransaction.hex()}")

    # Senden der Transaktion
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f'Transaktion gesendet, TX Hash: {tx_hash.hex()}')

    # Bestätigung der Transaktion abwarten
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f'Transaktion bestätigt in Block {receipt.blockNumber}')
# sixD()
def sixE():
    def extract_public_key(tx):
        signed_message = encode_defunct(hexstr=tx['hash'].hex())
        signature = {
            'v': tx['v'],
            'r': web3.to_hex(tx['r']),
            's': web3.to_hex(tx['s'])
        }
        public_key = Account.recover_message(signed_message, vrs=(signature['v'], signature['r'], signature['s']))
        return public_key

    # Liste, um die Public Keys zu speichern
    public_keys = []

    # Endblocknummer (kann durch den aktuellen Block oder einen anderen spezifischen Block ersetzt werden)
    end_block_number = web3.eth.block_number
    count= 0
    # Durchlaufen der Blöcke
    for block_number in range(0, 1989):
        block = web3.eth.get_block(block_number, full_transactions=True)
        for tx in block.transactions:
            try:
                public_key = extract_public_key(tx)
                public_keys.append(public_key)
                print(f"CountAppended: {count}; blockNumber: {block_number}")
                count +=1
            except Exception as e:
                print(f"Fehler beim Extrahieren des Public Keys für Transaktion {tx['hash'].hex()}: {e}")
        print(f"blockNumber: {block_number}")

    # Alle gefundenen Public Keys anzeigen
    print(f"Gefundene Public Keys bis Block 1989:")
    for pk in public_keys:
        print(pk)
sixE()
def sixB():
    # Adressen und private Schlüssel der Wallets
    source_address = "0x30DBFde92c0d62584597094C436FC241278DbbDc"
    target_address = "0x3b5A5B160EeaD4918bd2D132aBf8665d019F861D"
    private_key = "da5718ac70daadfe1faf1e55d27dbebc917e7f88430b6b892f967712c029802a"

    # Adresse aus dem privaten Schlüssel berechnen
    calculated_address = web3.eth.account.from_key(private_key).address

    if calculated_address.lower() != source_address.lower():
        print(f"Fehler: Die berechnete Adresse {calculated_address} stimmt nicht mit der angegebenen Quelladresse {source_address} überein.")
        exit()

    print(f"Berechnete Adresse aus dem privaten Schlüssel: {calculated_address}")

    # Kontostand überprüfen
    balance = web3.eth.get_balance(source_address)
    print(f"Kontostand von {source_address}: {web3.from_wei(balance, 'ether')} Ether")

    # Betrag für jede Transaktion (in Wei)
    amount = web3.to_wei(0.01, 'ether')  # Beispiel: 0.01 Ether pro Transaktion

    # Gaspreis und Gaslimit festlegen
    gas_price = web3.to_wei(50, 'gwei')  # Beispiel: 50 Gwei
    gas_limit = 21000  # Standard für einfache ETH-Transaktionen

    # Chain ID für Replay Protection (z.B. 15 für ein privates Netzwerk)
    chain_id = 108

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
        
        try:
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(f'Transaktion gesendet, TX Hash: {tx_hash.hex()}')
        except ValueError as e:
            print(f"Fehler beim Senden der Transaktion: {e}")

    # Senden von 1000 Transaktionen
    nonce = web3.eth.get_transaction_count(source_address)
    for i in range(1000):
        try:
            send_transaction(nonce + i)
        except Exception as e:
            print(f"Fehler bei Transaktion {i+1}: {e}")
        # Optional: kleine Pause zwischen den Transaktionen
        time.sleep(0.1)

    print("1000 Transaktionen erfolgreich gesendet")
