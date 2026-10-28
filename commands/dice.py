import random

from discord.ext import commands
from commands.base.command import Command


class Dice(Command):
    def __init__(self):
        super().__init__(
            name="dice",
            brief_description=f"Rolls a dice",
            extended_description="Rolls a dice with specified amount of sides",
            arguments_description={
                "x":  "Dice with x sides",
            },
            aliases=["roll"],
        )

    @staticmethod
    async def execute(ctx, sides: int):
        result = str(random.randint(1, sides))
        await ctx.send(result)

    @staticmethod
    async def handle_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Please provide amount of sides! Example: `!dice 6`")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Not a valid dice!")
        else:
            raise error

    def get_handler(self):
        async def handler(ctx, sides: int):
            if not self.enabled:
                await ctx.send(f"❌ {self.name} is disabled")
                return
            try:
                await self.execute(ctx, sides)
            except commands.BadArgument as e:
                await self.handle_error(ctx, e)
        return handler