from discord.ext import commands
from bot import bot

@bot.command()
async def calculator(ctx, a: int, b: int):
    result = a + b

    if result == 67:
        result = "6🤷🏻‍♀️7"

    await ctx.send(result)

@calculator.error
async def calculator_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Please provide two numbers! Example: `!calculator 30 37`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Both arguments must be integers.")
    else:
        raise error