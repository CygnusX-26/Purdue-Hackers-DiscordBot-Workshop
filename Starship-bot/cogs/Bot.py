import os
import discord
from discord.ext import commands


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
        channel: int = int(os.getenv('channel'))
        if channel == None:
            return
        channel = discord.utils.get(self.bot.get_all_channels(), id=int(channel))
        if len(reaction.message.reactions) >= 1:
            embed = discord.Embed(
                title=f"{reaction.message.author}'s message is on a roll!",
                description=f"{reaction.message.content}",
                color=discord.Colour.dark_blue()
            )
            embed.set_footer(text=f"{reaction.emoji}: {len(reaction.message.reactions)}")
            await channel.send(embed=embed)
             


async def setup(bot: commands.Bot):
    await bot.add_cog(Bot(bot))