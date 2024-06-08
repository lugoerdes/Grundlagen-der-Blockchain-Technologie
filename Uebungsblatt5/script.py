import binascii
from decimal import Decimal
import string
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# RPC-Zugangsdaten (anpassen)
rpc_user = "kuhmist123"
rpc_password = "kuhmist1234"
host = "127.0.0.1"  # oder die IP-Adresse deiner Node
port = 18443  # Port im Regtest-Modus
wallet_name = "LastOne"
node_address = '144.91.79.46:1800'

def connect_to_node(rpc_user, rpc_password, host='127.0.0.1', port=18443):
    # Erstelle die Verbindungs-URL
    rpc_url = f"http://{rpc_user}:{rpc_password}@{host}:{port}"
    
    # Verbinde zur Node
    rpc_connection = AuthServiceProxy(rpc_url)
    return rpc_connection

# Verbinde zur Node
rpc_connection = connect_to_node(rpc_user, rpc_password, host, port)

def main():
    try:
        # Beispiel für einen RPC-Aufruf: Hole die Blockchain-Info
        blockchain_info = rpc_connection.getblockchaininfo()
        print("Blockchain Info:", blockchain_info)

        # Beispiel für einen weiteren RPC-Aufruf: Hole die Bestätigung der letzten Blockhöhe
        block_count = rpc_connection.getblockcount()
        print("Block Count:", block_count)

        peers = rpc_connection.getpeerinfo()
        
        if peers:
            print("Der Node ist bereits mit anderen Nodes verbunden.")
        else:
            print("Keine Verbindung zu anderen Nodes. Füge neuen Node hinzu...")
            rpc_connection.addnode(node_address, 'add')
            print(f"Node {node_address} erfolgreich hinzugefügt.")
        wallets = rpc_connection.listwallets()
        if wallets:
            print(f"Wallet geladen {wallets}")
        else:
            print("Keine Wallet geladen. Lade Wallet...")
            rpc_connection.loadwallet(wallet_name)
            print(f"Wallet '{wallet_name}' erfolgreich geladen.")

    except JSONRPCException as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def getTotalBalance():
    try:
        # Abfragen der bestätigten und unbestätigten Guthaben der Wallet
        balances = rpc_connection.getbalances()
        confirmed_balance = balances['mine']['trusted']
        unconfirmed_balance = balances['mine']['untrusted_pending']
        print(f"Bestätigtes Guthaben: {confirmed_balance} BTC")
        print(f"Unbestätigtes Guthaben: {unconfirmed_balance} BTC")
    except JSONRPCException as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def getListaddressgroupings():
    listaddressgroupings = rpc_connection.listaddressgroupings() 
    print("Listaddressgroupings: " , listaddressgroupings) 

#ALT def saveTextToTransaction(text,to_address, change_address, amount):
#     try:
#          # Text in Hex umwandeln
#         hex_data = binascii.hexlify(text.encode('utf-8')).decode('utf-8')
#         # UTXOs (Unspent Transaction Outputs) auflisten
#         utxos = rpc_connection.listunspent()
#         print(utxos)

#         # Die UTXOs für die Eingaben auswählen
#         inputs = [{"txid": utxo["txid"], "vout": utxo["vout"]} for utxo in utxos]

#         # Die Ausgaben der Transaktion
#         total_utxo_amount = sum(Decimal(utxo['amount']) for utxo in utxos)
#         outputs = {to_address: Decimal(amount), change_address: total_utxo_amount - Decimal(amount) - Decimal(
#             "0.0001")}  # Sende den Rest an die change_address abzüglich einer kleinen Gebühr

#         # OP_RETURN Output hinzufügen
#         outputs["data"] = hex_data
#         # Erstellen der Rohtransaktion
#         raw_tx = rpc_connection.createrawtransaction(inputs, outputs)

#         # Signieren der Rohtransaktion
#         signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)

#         if not signed_tx.get("complete"):
#             raise Exception("Transaktion konnte nicht signiert werden")

#         # Senden der signierten Transaktion
#         tx_id = rpc_connection.sendrawtransaction(signed_tx["hex"])

#         print(f"Transaktion erfolgreich gesendet! Transaktions-ID: {tx_id}")
#         return tx_id

#     except JSONRPCException as e:
#         print(f"Ein Fehler ist aufgetreten: {e}")
#     except Exception as e:
#         print(f"Ein Fehler ist aufgetreten: {e}")


def send_transaction(to_address, amount):
     try:
        # Überprüfen Sie, ob die Adresse gültig ist
        if not rpc_connection.validateaddress(to_address)['isvalid']:
            return f"Ungültige Adresse: {to_address}"
        
        # Sende die Transaktion
        txid = rpc_connection.sendtoaddress(to_address, amount)
        print(f"Transaktion erfolgreich gesendet! TXID: {txid}")
     except JSONRPCException as e:
        print(f"Fehler beim Senden der Transaktion: {e}")

#NEU def saveTextToTransaction(text,empfaenger_adresse, betrag):
#     try:
#         # OP_RETURN-Daten vorbereiten
#         op_return_data = binascii.hexlify(text.encode('utf-8')).decode('utf-8')
        
#         # Transaktionseingänge und -ausgänge vorbereiten
#         inputs = [{"txid": utxo['txid'], "vout": utxo['vout']} for utxo in utxos]
#         outputs = {empfaenger_adresse: betrag, 'data': op_return_data}
        
#         # Wechselgeld berechnen
#         wechselgeld = gesamtbetrag - betrag
#         if wechselgeld > 0:
#             outputs[rpc_connection.getrawchangeaddress()] = wechselgeld
        
#         # Transaktion erstellen
#         raw_tx = rpc_connection.createrawtransaction(inputs, outputs)
        
#         # Transaktion signieren
#         signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)
        
#         # Transaktion senden
#         txid = rpc_connection.sendrawtransaction(signed_tx['hex'])
        
#         return f"Transaktion erfolgreich gesendet! TXID: {txid}", txid
#     except JSONRPCException as e:
#         return f"Fehler beim Senden der Transaktion: {e}", None

def finde_op_return_transaktionen(rpc_connection):
    try:
        blockchain_info = rpc_connection.getblockchaininfo()
        aktuelle_blockhoehe = blockchain_info['blocks']
        op_return_transaktionen = []

        for hoehe in range(0, aktuelle_blockhoehe + 1):
            block_hash = rpc_connection.getblockhash(hoehe)
            block = rpc_connection.getblock(block_hash, 2)  # 2: Block und Transaktionen als JSON
            for tx in block['tx']:
                for vout in tx['vout']:
                    if 'scriptPubKey' in vout and vout['scriptPubKey']['type'] == 'nulldata':
                        op_return_hex = vout['scriptPubKey']['asm'].split(' ')[1]
                        try:
                            op_return_data = binascii.unhexlify(op_return_hex).decode('utf-8')
                            # Überprüfen, ob der Text lesbar ist (nur ASCII-Zeichen)
                            if all(c in string.printable for c in op_return_data):
                                op_return_transaktionen.append({
                                    'txid': tx['txid'],
                                    'block_height': hoehe,
                                    'op_return_data': op_return_data
                                })
                        except (binascii.Error, UnicodeDecodeError):
                            # Ignorieren, wenn die Hex-Daten nicht zu Klartext dekodiert werden können
                            continue
            print(f"Block {hoehe}/{aktuelle_blockhoehe} verarbeitet.")
        
        return op_return_transaktionen

    except JSONRPCException as e:
        print(f"Fehler beim Durchsuchen der Blockchain: {e}")
        exit()


main()
# Suche nach OP_RETURN-Transaktionen
op_return_transaktionen = finde_op_return_transaktionen(rpc_connection)

# Ausgabe der gefundenen Transaktionen
for tx in op_return_transaktionen:
    print(f"TXID: {tx['txid']}, Blockhöhe: {tx['block_height']}, OP_RETURN-Daten: {tx['op_return_data']}")



# getListaddressgroupings()
# send_transaction("bcrt1qejvcjrmfm9xg460wzuwnfsngl7x6nd64xf5vjf", 0.0005)
# getwalletinfo()
# # getTotalBalance()
# text = "Dies ist ein Test."
# saveTextToTransaction("Wenn ich Doctor wäre, wäre ich Doctor G.","bcrt1qejvcjrmfm9xg460wzuwnfsngl7x6nd64xf5vjf", 0.0001)