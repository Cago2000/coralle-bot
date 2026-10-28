from discord.ext import commands
import discord
import constants


class CustomHelpCommand(commands.DefaultHelpCommand):
    def __init__(self, **options):
        super().__init__(**options)
        self.no_category = "Commands"

    def format_commands(self, commands_list):
        if not commands_list:
            return ""

        lines = []
        commands_list.sort(key=lambda x: x.qualified_name)
        for cmd in commands_list:
            if cmd.qualified_name == "help":
                cmd_subclass = constants.command_subclass_mapping.get("help")
                brief = cmd_subclass.brief_description if cmd_subclass else "No description"
            else:
                brief = cmd.brief or "No description"
            lines.append(f"{cmd.qualified_name:<10} : {brief}")

        return "```\n" + "\n".join(lines) + "\n```"

    async def send_bot_help(self, mapping):
        bot_commands = []
        for cog, cog_commands in mapping.items():
            bot_commands.extend(
                cmd for cmd in cog_commands
                if not cmd.hidden
            )

        commands_text = self.format_commands(bot_commands)
        description = f"Commands:\n{commands_text}\n\nType `!help command` for more info on a command."

        embed = discord.Embed(
            description=description,
            color=discord.Color.blurple()
        )

        await self.get_destination().send(embed=embed)

    def get_command_metadata(self, command):
        extras = getattr(command, 'extras', {})
        if 'arguments' in extras:
            return {
                "description": command.help or "No description given",
                "arguments": extras.get('arguments', {})
            }

        cmd_subclass = constants.command_subclass_mapping.get(command.qualified_name)
        if cmd_subclass:
            return {
                "description": cmd_subclass.extended_description or "No description given",
                "arguments": cmd_subclass.arguments_description
            }

        return {}

    async def send_command_help(self, command):
        metadata = self.get_command_metadata(command)
        description = metadata.get("description", "No description given")
        argument_descriptions = metadata.get("arguments", {})

        aliases_text = ""
        if command.aliases:
            aliases_str = "|".join(command.aliases)
            aliases_text = f"Aliases: ![{aliases_str}]"

        example_text = ""
        if argument_descriptions:
            args_placeholder = " ".join(f"{{{arg}}}" for arg in argument_descriptions.keys())
            example_text = f"Example: !{command.qualified_name} {args_placeholder}"

        arguments_text = ""
        if argument_descriptions:
            arguments_text = "Arguments:\n"
            for param_name, param_desc in argument_descriptions.items():
                arguments_text += f"  {param_name}: {param_desc}\n"

        parts = [description]
        if aliases_text:
            parts.append(aliases_text)
        if example_text:
            parts.append(example_text)
        if arguments_text:
            parts.append(arguments_text)

        full_description = "\n\n".join(parts)

        embed = discord.Embed(
            title=f"Command: {command.qualified_name}",
            description=full_description,
            color=discord.Color.blurple()
        )

        await self.get_destination().send(embed=embed)