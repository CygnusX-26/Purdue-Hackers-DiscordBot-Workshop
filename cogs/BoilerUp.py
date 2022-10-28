import discord
from discord.ext import commands
from discord import app_commands


class BoilerUp(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name= 'boiler', description = 'BOILER UP!')
    async def boiler(self, interaction: discord.Interaction, text: str) -> None:
        await interaction.response.send_message(f"{text}!", ephemeral=True)



async def setup(bot: commands.Bot):
    await bot.add_cog(BoilerUp(bot))