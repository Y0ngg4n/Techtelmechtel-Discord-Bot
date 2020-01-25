import discord
from discord.ext import commands

import random
import json


class Kiss(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.json = json.load(open("url.json", "r"))

    def kiss_embed(self, position, user, author):
        message = f"{author.name} kisses the {position} " \
                  f"of {user.mention}" if position != "main" else f"{author.name} kisses {user.mention}"
        embed = discord.Embed(description=message)
        embed.set_image(url=random.choice(self.json["kiss"][position]))
        return embed

    @commands.group(name="kiss", aliases=["k"], invoke_without_command=True)
    async def _kiss(self, ctx, user: discord.User):
        await ctx.send(embed=self.kiss_embed("main", user, ctx.author))

    @_kiss.command(name="mouth", aliases=["m", "mouths", "mund"])
    async def _kiss_mouth(self, ctx, user: discord.User):
        await ctx.send(embed=self.kiss_embed("mouth", user, ctx.author))

    @_kiss.command(name="neck", aliases=["n", "necks", "nacken"])
    async def _kiss_neck(self, ctx, user: discord.User):
        await ctx.send(embed=self.kiss_embed("neck", user, ctx.author))

    @_kiss.command(name="hand", aliases=["h", "hands"])
    async def _kiss_hand(self, ctx, user: discord.User):
        await ctx.send(embed=self.kiss_embed("hand", user, ctx.author))

    @_kiss.command(name="cheek", aliases=["c", "cheeks", "wange", "backe"])
    async def _kiss_cheek(self, ctx, user: discord.User):
        await ctx.send(embed=self.kiss_embed("cheek", user, ctx.author))

    @_kiss.command(name="breast", aliases=["b", "breasts", "brust"])
    async def _kiss_breast(self, ctx, user: discord.User):
        await ctx.send(embed=self.kiss_embed("breast", user, ctx.author))


def setup(bot: commands.Bot):
    bot.add_cog(Kiss(bot))
