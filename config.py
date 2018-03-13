#bot configuration
bot_prefix = "!"        # Enter your desired prefix here (e.g. !)
bot_token = ""          # Enter bot token here
bot_channel_id = ""     # Enter a channel id here to specify which channel the bot goes to

#wallet configuration
rpc_user = ''         # Enter rpcuser here
rpc_password = ''   # Enter rpcpass here
rpc_port =             # Enter rpcport here (int)

# static list of the available commands
command_list = {'my':
                    {
                        'balance':'Retrieve your current total balance = deposit + stake - withdrawals',
                        'address':'Retrieve all your receiving addresses including the total amount deposited for each address',
                        'transaction':'List all your last 10 transactions showing the amount and the category'
                    },
                'bot':
                    {
                        'help':'list all the commands available'
                    }
                }