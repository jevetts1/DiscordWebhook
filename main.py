import pandas as pd
import discord

client = discord.Client()
guild = discord.Guild

def isCommand(message):
    if message.content.startswith(";;"):
        return True
    
    return False

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith(";;"):
        command = message.content[2:].split()[0]

        params = []

        if len(message.content.split()) > 1:
            params = (message.content.split()[1:])

    if command == "help":
        channel = message.channel
        await channel.send("Read functionality:\n;;read <number of messages to read> <file save location>")

    if command == "read":
        channel = message.channel
        await channel.send("Reading messages...")

        data = pd.DataFrame(columns = ["content","time","author"])

        if len(params) != 0:
            limit = int(params[0])

        else:
            limit = 100

        async for m in message.channel.history(limit = limit):
            if m.author != client.user:
                if not isCommand(m):
                    data = data.append({"content":m.content,"time":m.created_at,"author":m.author.name},ignore_index = True)

            if len(data) == limit:
                break
        
        if len(params) >= 2:
            params[1] = params[1].replace("\\","/") + "/data.csv"

            fileLocation = params[1]

        else:
            fileLocation = "C:/data.csv"

        data.to_csv(fileLocation)

client.run("MTAwMzcyMjg2NTQ4MjQwMzg4MA.Ggsobl.GywRTRD9G-rbNA8s1Mb-Lx65n_HpUhaHOrMBbg")