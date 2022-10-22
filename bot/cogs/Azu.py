import discord
from discord.ext import commands
from discord import app_commands


class Azu(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  #help command
  @app_commands.command(name='azu', description='One boingy boi')
  async def azu(self, interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
      "https://media.discordapp.net/attachments/404119744107773974/1030001510106542100/F696304B-A1E2-4003-B2B6-9BBB352FFB31.gif"
    )


async def setup(bot: commands.Bot):
  await bot.add_cog(Azu(bot))

