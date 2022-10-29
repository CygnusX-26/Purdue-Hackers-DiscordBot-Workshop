import discord
from discord.ext import commands
from discord import app_commands
import os


class SetChannel(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @app_commands.command(name= 'setchannel', description = 'Sets your channel!')
    async def setchannel(self, interaction: discord.Interaction, channel: discord.TextChannel) -> None:
        os.environ['channel'] = str(channel.id)
        await interaction.response.send_message(f"Set your channel to {channel.mention}!!", ephemeral=True)



async def setup(bot: commands.Bot):
    await bot.add_cog(SetChannel(bot))