import discord
from commands.base.command import Command
import constants


class Help(Command):
    def __init__(self):
        super().__init__(
            name="help",
            brief_description="Shows this message",
            extended_description="Shows this message and explains commands",
            arguments_description={
                "command": "Command you need help with"
            },
            aliases=["helpme"],
        )

    async def execute(self, ctx, *, command):
        if command is None:
            await self.execute_overview_help(ctx)
        else:
            await self.execute_command_help(ctx, command)

    @staticmethod
    async def execute_overview_help(ctx):
        commands = sorted(
            (cmd for cmd in ctx.bot.commands if not cmd.hidden),
            key=lambda cmd: cmd.qualified_name,
        )

        lines = []
        for cmd in commands:
            brief = (
                constants.command_subclass_mapping["help"].brief_description
                if cmd.qualified_name == "help" and "help" in constants.command_subclass_mapping
                else cmd.brief or "No description"
            )
            lines.append(f"{cmd.qualified_name:<10} : {brief}")

        description = (
            "Commands:\n```\n" + "\n".join(lines) +
            "\n```\n\nType `!help [command]` for more info on a command."
            if lines else ""
        )

        await ctx.send(embed=discord.Embed(
            description=description,
            color=discord.Color.blurple(),
        ))

    @staticmethod
    async def execute_command_help(ctx, command: str):
        cmd = ctx.bot.get_command(command)
        if cmd is None:
            await ctx.send(f"Command `{command}` not found")
            return

        parts = []
        parts.append(f"Description:\n```{cmd.help or 'No description'}```")
        parts.append("Aliases:\n" + " ".join(f"```{alias}```" for alias in cmd.aliases or ["No aliases"]))
        arguments = cmd.extras.get("arguments", {})
        if arguments:
            args_placeholder = " ".join(f"{{{arg}}}" for arg in arguments)
            parts.extend([
                f"Example:\n```!{cmd.qualified_name} {args_placeholder}```",
                "Arguments:\n```\n" + "\n".join(
                    f"{name}: {desc}" for name, desc in arguments.items()
                ) + "\n```",
            ])
        else:
            parts.append("Arguments:\n ```No arguments```")

        embed = discord.Embed(
            title=f"Command: {cmd.qualified_name}",
            description="\n\n".join(parts),
            color=discord.Color.blurple(),
        )
        await ctx.send(embed=embed)

    def get_handler(self):
        async def handler(ctx, *, command: str = None):
            if not self.enabled:
                await ctx.send(f"Command ´{self.name}´ is disabled")
                return
            await self.execute(ctx, command=command)
        return handler