
#!/usr/bin/python3
import json
import requests
import sqlite3
from bloxplorer import bitcoin_explorer
import sys
import time

conn = sqlite3.connect('bitcoin.db')
c = conn.cursor()

api_url_base = 'https://chain.api.btc.com/v3/block/'

latest_height= bitcoin_explorer.blocks.get_last_height().data
print(latest_height)

startBlock= int(sys.argv[1])
endBlock = int(sys.argv[2])

for x in range(startBlock,endBlock):
    api_url=api_url_base+str(x)
    response = requests.get(api_url)
    if response.status_code == 200:
        block = json.loads(response.content.decode('utf-8'))['data']
        txs = bitcoin_explorer.blocks.get_txids(block['hash'])   
        c.execute("insert into blocks values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [
        block['height'],
        block['version'],
        block['mrkl_root'],
        block['timestamp'],
        block['bits'],
        block['nonce'],
        block['hash'],
        block['prev_block_hash'],
        block['next_block_hash'],
        block['size'],
        block['pool_difficulty'],
        block['difficulty'],
        block['difficulty_double'],
        block['tx_count'],
        block['reward_block'],
        block['reward_fees'],
        block['confirmations'],
        block['is_orphan'],
        block['curr_max_timestamp'],
        block['is_sw_block'],
        block['stripped_size'],
        block['sigops'],
        block['weight'],
        json.dumps(block['extras']),
        0,0,"non","nan",json.dumps(txs.data)])
        conn.commit()
        time.sleep(5)

