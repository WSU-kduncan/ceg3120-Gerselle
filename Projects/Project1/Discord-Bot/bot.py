import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

    # User says this
    greetings = ["Hello!", "Hi!", "Hey!"]

    # Bot responds with "Hello!" in 9 languages (ES, FR, JP, KR, RU, ZH-CN, TL, AR, DE)
    hey_there = ["¡Hola!", "Bonjour!", "こんにちは!", "여보세요!", "Привет!", "你好!", "Kamusta!", "مرحبا!", "Grüß Gott!"]

    if message.content == 'towel!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)
    
    # Greeting command
    elif message.content in greetings:
        response = random.choice(hey_there)
        await message.channel.send(response)
  
    # Picture command
    if message.content == 'What do you have?':
        image = random.choice("123456789") + ".jpg"
        await message.channel.send(file=discord.File(image))

client.run(TOKEN)
