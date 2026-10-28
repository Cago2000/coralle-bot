from discord.ext import commands
import discord


class CustomHelpCommand(commands.DefaultHelpCommand):
    def __init__(self, **options):
        super().__init__(**options)
        self.no_category = "Commands"
        self.help = "Shows this message"



    def format_commands(self, commands_list):
        if not commands_list:
            return ""

        lines = []
        for cmd in commands_list:
            if cmd.qualified_name == "help":
                brief = self.help
            else:
                brief = cmd.brief or "No description"
            lines.append(f"  {cmd.qualified_name:<14}: {brief}")

        return "\n".join(lines)

    async def send_bot_help(self, mapping):
        bot_commands = []
        for cog, cog_commands in mapping.items():
            bot_commands.extend(
                cmd for cmd in cog_commands
                if not cmd.hidden
            )

        commands_text = self.format_commands(bot_commands)
        description = f"Commands:\n{commands_text}\n\nType !help command for more info on a command."

        embed = discord.Embed(
            description=description,
            color=discord.Color.blurple()
        )

        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        description = command.help or "No description given"
        signature = self.get_command_signature(command)

        arguments_text = ""
        if command.clean_params:
            arguments_text = "Arguments:\n"
            for param_name, param in command.clean_params.items():
                param_desc = param.description or "No description given"
                arguments_text += f"  {param_name} {param_desc}\n"

        full_description = f"{signature}\n\n{description}"
        if arguments_text:
            full_description += f"\n\n{arguments_text}"

        embed = discord.Embed(
            title=command.qualified_name,
            description=full_description,
            color=discord.Color.blurple()
        )

        await self.get_destination().send(embed=embed)