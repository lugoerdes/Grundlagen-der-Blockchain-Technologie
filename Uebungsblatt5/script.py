import binascii
from decimal import Decimal
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# RPC-Zugangsdaten (anpassen)
rpc_user = "kuhmist123"
rpc_password = "kuhmist1234"
host = "127.0.0.1"  # oder die IP-Adresse deiner Node
port = 18443  # Port im Regtest-Modus


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
        
    except JSONRPCException as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


def send_transaction(to_address, change_address, amount):
    try:
        # UTXOs (Unspent Transaction Outputs) auflisten
        utxos = rpc_connection.listunspent()
        print(utxos)

        # Die UTXOs für die Eingaben auswählen
        inputs = [{"txid": utxo["txid"], "vout": utxo["vout"]} for utxo in utxos]

        # Die Ausgaben der Transaktion
        total_utxo_amount = sum(Decimal(utxo['amount']) for utxo in utxos)
        outputs = {to_address: Decimal(amount), change_address: total_utxo_amount - Decimal(amount) - Decimal(
            "0.0001")}  # Sende den Rest an die change_address abzüglich einer kleinen Gebühr

        # Erstellen der Rohtransaktion
        raw_tx = rpc_connection.createrawtransaction(inputs, outputs)

        # Signieren der Rohtransaktion
        signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)

        if not signed_tx.get("complete"):
            raise Exception("Transaktion konnte nicht signiert werden")

        # Senden der signierten Transaktion
        tx_id = rpc_connection.sendrawtransaction(signed_tx["hex"])

        print(f"Transaktion erfolgreich gesendet! Transaktions-ID: {tx_id}")
        return tx_id

    except JSONRPCException as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    except Exception as e:
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

def saveTextToTransaction(text,to_address, change_address, amount):
    try:
         # Text in Hex umwandeln
        hex_data = binascii.hexlify(text.encode('utf-8')).decode('utf-8')
        # UTXOs (Unspent Transaction Outputs) auflisten
        utxos = rpc_connection.listunspent()
        print(utxos)

        # Die UTXOs für die Eingaben auswählen
        inputs = [{"txid": utxo["txid"], "vout": utxo["vout"]} for utxo in utxos]

        # Die Ausgaben der Transaktion
        total_utxo_amount = sum(Decimal(utxo['amount']) for utxo in utxos)
        outputs = {to_address: Decimal(amount), change_address: total_utxo_amount - Decimal(amount) - Decimal(
            "0.0001")}  # Sende den Rest an die change_address abzüglich einer kleinen Gebühr

        # OP_RETURN Output hinzufügen
        outputs["data"] = hex_data
        # Erstellen der Rohtransaktion
        raw_tx = rpc_connection.createrawtransaction(inputs, outputs)

        # Signieren der Rohtransaktion
        signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)

        if not signed_tx.get("complete"):
            raise Exception("Transaktion konnte nicht signiert werden")

        # Senden der signierten Transaktion
        tx_id = rpc_connection.sendrawtransaction(signed_tx["hex"])

        print(f"Transaktion erfolgreich gesendet! Transaktions-ID: {tx_id}")
        return tx_id

    except JSONRPCException as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def getListaddressgroupings():
    listaddressgroupings = rpc_connection.listaddressgroupings() 
    print("Listaddressgroupings: " , listaddressgroupings) 

main()
# getListaddressgroupings()
send_transaction("bcrt1qx03gsqprkd406n7aversk8er8670n0mt3nw962", "bcrt1qx03gsqprkd406n7aversk8er8670n0mt3nw962", 0.005)
# # getTotalBalance()
# text = "Dies ist ein Test."
# saveTextToTransaction(text,"bcrt1qx03gsqprkd406n7aversk8er8670n0mt3nw962", "bcrt1qx03gsqprkd406n7aversk8er8670n0mt3nw962", 0.005)