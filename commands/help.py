from discord.ext import commands
import discord


class CustomHelpCommand(commands.DefaultHelpCommand):
    async def send_command_help(self, command):
        help_text = command.help or "No description given"

        arguments = command.extras.get('arguments', {})
        if arguments:
            help_text += "\n\nArguments:"
            for arg_name, arg_desc in arguments.items():
                help_text += f"\n  {arg_name}: {arg_desc}"

        title = f"!{command.name}"
        if command.aliases:
            title += f" | aliases: {', '.join(command.aliases)}"

        embed = discord.Embed(title=title, description=help_text)
        await self.context.send(embed=embed)