import random
import re

from discord.ext import commands
from commands.base.command import Command


class Dice(Command):
    def __init__(self):
        super().__init__(
            name="dice",
            brief_description=f"Rolls dice",
            extended_description="Rolls dice where `n` is the dice count and `x` the amount of sides",
            arguments_description={
                "ndx":  "n Dices with x sides",
            },
            aliases=["roll"],
        )

    @staticmethod
    async def execute(ctx, code: str):
        match = re.fullmatch(r"(\d+)d(\d+)", code.strip().lower())
        if not match:
            await ctx.send("Invalid format. `ndx`, "
                           "where `n` is the dice count "
                           "and `x` the amount of sides.")
            return
        count, sides = map(int, match.groups())
        if count < 1 or sides < 1:
            await ctx.send("Number of dice (`x` and sides (`n`) must be at least 1.")
            return

        header_str = f"**Rolling {code}!**:"
        roll_str_list = []
        rolls = {}

        for c in range(1, count + 1):
            roll = random.randint(1, sides)
            rolls[c] = roll
            roll_str_list.append(f"🎲 Rolling d{sides}...      ` {roll} `")

        sum_str = sum(rolls.values())
        result = "\n".join([header_str, *roll_str_list, f"➕ **Total: {sum_str}**"])
        await ctx.send(result)

    async def handle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please provide amount of sides! Example: `!{self.name} 2d6`")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Not a valid dice!")
        else:
            raise error

    def get_handler(self):
        async def handler(ctx, code: str):
            if not self.enabled:
                await ctx.send(f"{self.name} is disabled")
                return
            try:
                await self.execute(ctx, code)
            except commands.BadArgument as e:
                await self.handle_error(ctx, e)
        return handler