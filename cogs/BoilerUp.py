import discord
from discord.ext import commands
from discord import app_commands


class BoilerUp(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name= 'boiler', description = 'BOILER UP!')
    async def boiler(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("up!", ephemeral=True)

    @app_commands.command(name= 'purduehackers', description = '!!!!')
    async def puhackers(self, interaction: discord.Interaction, text:str, channel: discord.TextChannel) -> None:
        await interaction.response.send_message(f"!!!! check {channel.name} for {text}", ephemeral=True)
        await channel.send(text)


async def setup(bot: commands.Bot):
    await bot.add_cog(BoilerUp(bot))