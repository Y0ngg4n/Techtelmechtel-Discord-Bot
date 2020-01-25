import os
from discord.ext import commands

bot = commands.Bot(command_prefix=("?", "!", "."), case_insensitive=True)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

MODULES = ["kiss"]

for module in MODULES:
    bot.load_extension(module)

bot.run(os.getenv('DISCORD_TOKEN'))

