from decimal import Decimal

from discord.ext import commands
from commands.base.command import Command


class Sum(Command):
    def __init__(self):
        super().__init__(
            name="sum",
            brief_description=f"Adds 2 numbers together",
            extended_description="Adds 2 numbers together",
            arguments_description={
                "a": "First number",
                "b": "Second number"
            },
            aliases=["calc", "calculate"],
        )

    @staticmethod
    async def execute(ctx, a: float, b: float):
        a_str, b_str = str(a), str(b)
        result = Decimal(a_str) + Decimal(b_str)
        if result == 67.0:
            result = "6🤷🏻‍♀️7"
        if result == 69.0:
            result = "nice"
        await ctx.send(result)

    async def handle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please provide two numbers! Example: `!{self.name} 30 37`")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Both arguments must be numbers.")
        else:
            raise error

    def get_handler(self):
        async def handler(ctx, a: float, b: float):
            if not self.enabled:
                await ctx.send(f"{self.name} is disabled")
                return
            try:
                await self.execute(ctx, a, b)
            except commands.BadArgument as e:
                await self.handle_error(ctx, e)
        return handler