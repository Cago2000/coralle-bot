from bot import bot

@bot.command()
async def message(ctx, msg: str):
    await ctx.send(msg)