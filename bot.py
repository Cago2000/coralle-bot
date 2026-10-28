from discord.ext import commands
import discord
from overrides.help import CustomHelpCommand

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.help_command = CustomHelpCommand()