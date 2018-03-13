import discord
import logging
from  config import *
from discord.ext import commands
from bitcoinrpc.authproxy import AuthServiceProxy
from datetime import datetime

logging.basicConfig(filename='errors.log', level=logging.INFO)

# Creating the client object
client = commands.Bot(command_prefix=bot_prefix)


def getconn():
    conn = AuthServiceProxy('http://{0}:{1}@127.0.0.1:{2}'.format(rpc_user, rpc_password, rpc_port))
    return conn

connector = getconn()


# Prints the client login details in the terminal
@client.event
async def on_ready():
    print('---------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("Bot online")
    print('---------')

# Serves as the base command for commands about the bot
@client.group(pass_context=True)
async def bot(ctx):
    if ctx.invoked_subcommand is None or ctx.invoked_subcommand.name not in command_list['bot']:
        await client.say(
            "<@{}>, Invalid option. Supported options are !bot( {} )".format(ctx.message.author.id, ' | '.join(command_list['bot'])))

# It shows the available commands for the bot
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="",
                          description="", color=0x00924c)
    embed.set_author(
        name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
        icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))

    data = {}
    for category in command_list:
        record = ""
        for command, desc in command_list[category].items():
            record = record + "`" + "{0:>3} {1:<8} : {2: <20}".format(u"\u26AA", command, desc) + "`" + "\n"
        data[category] = record


    for item in data:
        embed.add_field(name="{0:>3} {1: <3}".format("!", item), value=data[item], inline=False)

    await client.send_message(ctx.message.author, embed=embed)

# Serves as the base command for commands related to the wallet
# Checks the  validity of the subcommand
@client.group(pass_context=True)
async def my(ctx):
    if ctx.invoked_subcommand is None or ctx.invoked_subcommand.name not in command_list['my']:
        await client.say(
            "<@{}>, Invalid option. Supported options are !my ( {} )".format(ctx.message.author.id, ' | '.join(command_list['my'])))

# Retrieve your current total balance = deposit + stake - withdrawals
@my.command(pass_context=True)
async def balance(ctx):
    embed = discord.Embed(title="", description="", color=0x00924c)
    embed.set_author(
        name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
        icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))
    record = "`" + "{0:} : {1: <25,.8f}".format(u"\U0001F4B2", connector.getbalance()) + "`" + "\n"

    embed.add_field(name="Current Balance", value=record, inline=False)

    await client.send_message(ctx.message.author, embed=embed)


# Retrieve all your receiving addresses including the total amount deposited for each address
@my.command(pass_context=True)
async def address(ctx):
    embed = discord.Embed(title="",
                          description="", color=0x00924c)
    embed.set_author(
        name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
        icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))

    list = connector.listaddressgroupings()

    record = ""
    counter = 0
    data = []
    for item in list:
        for subitem in item:
            if len(subitem) != 3:
                subitem.append("No label")
            record = record + "`" + "{0:} : {1:} \u2003 {2:.8f} \u2003 {3:}".format(u'\U0001F4D2', subitem[0],
                                                                      subitem[1], subitem[2]) + "`" + "\n"
            counter = counter + 1
            if counter == 10:
                data.append(record)
                record = ""
                counter = 0

    for item in data:
        if data.index(item) == 0:
            name = "\u2003 {0: <25} \u2003 \u2003 \u2003 \u2003 \u2003 \u2003 \u2003 \u2003 \u2002 \u2002 {1: <40} \u2002 \u2002 {2: <50}".format("Receiving Address", "Total Deposit", "Label")
        else:
            name ="\u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 \u2796 "
        embed.add_field(name=name, value=item, inline=False)

    await client.send_message(ctx.message.author, embed=embed)


# List all your last 10 transactions showing the amount and the category
@my.command(pass_context=True)
async def transaction(ctx):
    embed = discord.Embed(title="",
                          description="", color=0x00924c)
    embed.set_author(
        name=ctx.message.author.name + "  |  Lorem ipsum dolor sit amet | consectetur adipiscing elit, sed do eiusmod",
        icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Delivered By " + client.user.name + " at " + str(datetime.now()))

    list = connector.listtransactions("*", 10, 0)

    record = ""
    for item in list:
        if item['category'] == 'stake' or item['category'] == 'generate':
            category = "stake"
        elif item['category'] == 'send':
            category = "withdraw"
        else:
            category = "deposit"

        if item['amount'] < 0:
            item['amount'] = item['amount'] * -1

        record = record + "`" + "{0:} : {1:}\u2003 {2:.3f} \u2003 {3:>5}".format(u"\U0001F4B0", item['address'],
                                                                                    item['amount'], category) + "`" + "\n"

    name = "{0: <25} \u2003 \u2003 \u2003 \u2003 \u2003 \u2003 \u2003 \u2003 \u2002  {1: <40} \u2002 \u2002 {2: <50}".format(
        "Transaction Address", "Amount", "Category")
    embed.add_field(name=name, value=record, inline=False)

    await client.send_message(ctx.message.author, embed=embed)


client.run(bot_token)
