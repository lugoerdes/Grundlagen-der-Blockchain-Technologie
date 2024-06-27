import binascii
from decimal import Decimal
import decimal
import json
import string
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import requests

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

# ALT def saveTextToTransaction(text,to_address, change_address, amount):
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
#         outputs = {to_address: Decimal(amount), change_address: total_utxo_amount - Decimal(amount)}  # Sende den Rest an die change_address abzüglich einer kleinen Gebühr

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

# def saveTextToTransaction(text, to_address, change_address, amount, fee):
#     try:
#         # Text in Hex umwandeln
#         hex_data = binascii.hexlify(text.encode('utf-8')).decode('utf-8')
        
#         # UTXOs (Unspent Transaction Outputs) auflisten
#         utxos = rpc_connection.listunspent()
#         print(utxos)

#         # Die UTXOs für die Eingaben auswählen
#         inputs = []
#         total_utxo_amount = Decimal(0)
#         for utxo in utxos:
#             inputs.append({"txid": utxo["txid"], "vout": utxo["vout"]})
#             total_utxo_amount += Decimal(utxo['amount'])
#             if total_utxo_amount >= Decimal(amount) + Decimal(fee):
#                 break

#         if total_utxo_amount < Decimal(amount) + Decimal(fee):
#             raise Exception("Nicht genügend Guthaben für die Transaktion verfügbar")

#         # Die Ausgaben der Transaktion
#         outputs = {to_address: Decimal(amount)}
#         change_amount = total_utxo_amount - Decimal(amount) - Decimal(fee)
#         if change_amount > 0:
#             outputs[change_address] = change_amount

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


main()

# Suche nach OP_RETURN-Transaktionen
# op_return_transaktionen = finde_op_return_transaktionen(rpc_connection)

# # Ausgabe der gefundenen Transaktionen
# for tx in op_return_transaktionen:
#     print(f"TXID: {tx['txid']}, Blockhöhe: {tx['block_height']}, OP_RETURN-Daten: {tx['op_return_data']}")



# getListaddressgroupings()
# send_transaction("bcrt1qejvcjrmfm9xg460wzuwnfsngl7x6nd64xf5vjf", 0.0005)
# getwalletinfo()
# # getTotalBalance()
# text = "Dies ist ein Test."
saveTextToTransaction("Wenn ich Doctor wäre, wäre ich Doctor G.","bcrt1qejvcjrmfm9xg460wzuwnfsngl7x6nd64xf5vjf","bcrt1q6mtlmvn68am0p9c5xnm4gake0a9mhtxugcldk2", 0.01,0.0001)