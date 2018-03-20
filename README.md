# crypto-discord-bot
[![PyPI](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)
[![PyPI](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)

This app shows how you can query your cryptocoin Qt desktop wallet and present the information using a discord bot. It taps into native bitcoin
core apis built-in on desktop qt wallets to get information. Three commands were used as an example how to use it:
- get your current total balance
- get your generated receiving addresses and the total amounts deposited for each address
- list your last 10 transactions showing the address, amount and the transaction type

This project uses Python and 
[discord.py](https://github.com/Rapptz/discord.py/) - the API wrapper for Discord written in Python.



## Prerequisites
- Python 3.4.2+
- `aiohttp` library
- `websockets` library
- discord.py extension
- python-bitcoinrpc extension

## Installation
- Python 3.4.2+ can be downloaded [here](https://www.python.org/)
- You can install the discord.py library without full voice support by running this on your command:
```
python3 pip install discord.py
```
- You can install the bitcoin-rpc by running this on your command:
```
python3 pip install python-bitcoinrpc
```

## Code
Note: In Python 3.4 you use:
- `@asyncio.coroutine` instead of `async def` and 
- `yield from` instead of `await`

## Update Configuration

### Bot

- `bot_token`
- `bot_channel_id`

### Desktop Qt Wallet
- rp cport
- rpc user
- rpc password

Note: Make sure to create or update the coin's conf file ("coinname".conf) setting the rpc properties listed above.
Also, in setting the rpc user and rpc password do not use generic words such as "username" or "password" or it will not work

## Run
```sh
$ python bot.py
```

## Scaling  Options
- Use more of the methods available in the api
- Use of database to store the values and use the bot to query it instead. This adds a layer of security to your wallet but it has
limitations.
- If you have more than one desktop qt wallets you can loop through all of them
