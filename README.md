# Bitcoin Blocks Dataset Collection 

Build dataset of Bitcoin blocks information as SQLITE database for analysis. 
The tables include block information and the list of included transaction ids.

Sample of collected Bitcoin Block
```
{ 
"height":2643,
"version":1,
"mrkl_root":"cbac6699494b537be62026b4ef5804374b42df491b11a33e86f61c9dfc4dafdb",
"timestamp":1233522061,
"bits":486604799,
"nonce":61961708,
"hash":"00000000aa5fb4e7d3cf35707a05efd16f219d85b2430bb537c56059eb6a5575",
"prev_block_hash":"00000000992fc36cb87322f89071bf6003a91f9ebf64b5c33caf6f0a792f8224",
"next_block_hash":"00000000d652307cc75e42d3d436e4d858ef808142ce3ddc4d7addcd33e55bc3",
"size":215,
"pool_difficulty":1,
"difficulty":1,
"difficulty_double":1,
"tx_count":1,
"reward_block":5000000000,
"reward_fees":0,
"confirmations":659249,
"is_orphan":false,
"curr_max_timestamp":1233522061,
"is_sw_block":false,
"stripped_size":215,
"sigops":4,
"weight":860,
"extras":{"pool_name":"unknown","pool_link":""}},
"err_code":0,"err_no":0,"message":"success","status":"success"}

```

## Install 

```
pip3 install bloxplorer
```

## Usage

```
python3 bitcoin.py
```
