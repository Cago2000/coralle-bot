# commands/help.py
import discord

from commands.base.command import Command


class Help(Command):
    def __init__(self):
        super().__init__(
            name="help",
            brief_description="Shows this message",
            extended_description="Shows this message and can explain commands",
            arguments_description=
            {
                "command": "Command, you need help with"
            },
            aliases = ["helpme"],
        )

    def get_handler(self):
        async def handler(self, ctx, command=None):
            if not self.enabled:
                await ctx.send(f"❌ {self.name} is disabled")
                return

            if command is None:
                # Show all commands
                pass
            else:
                # Show specific command help
                cmd = ctx.bot.get_command(command)
                if cmd is None:
                    await ctx.send(f"❌ Command `{command}` not found")
                    return

                embed = discord.Embed(
                    title=cmd.name,
                    description=cmd.help or "No description",
                    color=discord.Color.blurple()
                )
                await ctx.send(embed=embed)
        return handler