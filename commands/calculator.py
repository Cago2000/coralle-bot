from discord.ext import commands
from command import Command


class Calculator(Command):
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Add two numbers",
            aliases=["calc"],
        )

    @staticmethod
    async def execute(self, ctx, a: int, b: int):
        result = a + b
        if result == 67:
            result = "6🤷🏻‍♀️7"
        if result == 69:
            result = "nice"
        await ctx.send(result)

    @staticmethod
    async def handle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Please provide two numbers! Example: `!calculator 30 37`")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Both arguments must be integers.")
        else:
            raise error

    def get_handler(self):
        async def handler(ctx, a: int, b: int):
            if not self.enabled:
                await ctx.send(f"❌ {self.name} is disabled")
                return
            try:
                await self.execute(ctx, a, b)
            except commands.BadArgument as e:
                await self.handle_error(ctx, e)

        return handler