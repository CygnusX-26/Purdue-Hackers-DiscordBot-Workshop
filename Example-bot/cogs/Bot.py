import discord
from discord.ext import commands
from discord import app_commands


class Bot(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #what gets run when the bot starts
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game(f"Put your funny message here!"))
        print('This bot is online!')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.Member) -> None:
        if reaction.emoji == "👍":
            await reaction.message.channel.send(f"hello {user.name}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Bot(bot))