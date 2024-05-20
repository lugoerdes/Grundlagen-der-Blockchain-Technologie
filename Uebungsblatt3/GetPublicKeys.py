from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# RPC-Verbindungseinstellungen
rpc_user = 'kuhmist123'
rpc_password = 'kuhmist1234'
rpc_host = '0.0.0.0'
rpc_port = '18443'  # Port für Regtest (standardmäßig 18443)

# Verbindung aufbauen
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")

# Blockanzahl abrufen
block_count = rpc_connection.getblockcount()

# Durch alle Blöcke iterieren
for height in range(block_count + 1):
    block_hash = rpc_connection.getblockhash(height)
    block = rpc_connection.getblock(block_hash)
    
    # Transaktionen des Blocks durchgehen
    for tx_id in block['tx']:
        tx_details = rpc_connection.getrawtransaction(tx_id, True)
        
        # Transaktions-Eingaben durchgehen
        for vin in tx_details['vin']:
            if 'txid' in vin:
                # Die vorige Transaktion abrufen, um Zugriff auf die Ausgaben zu haben
                prev_tx = rpc_connection.getrawtransaction(vin['txid'], True)
                output = prev_tx['vout'][vin['vout']]
                script_pub_key = output['scriptPubKey']
                
                # Prüfen, ob ein öffentlicher Schlüssel vorhanden ist
                if 'pubkeys' in script_pub_key:
                    print(f"Öffentlicher Schlüssel gefunden: {script_pub_key['pubkeys']}")
