from command import Command


class Message(Command):
    def __init__(self):
        super().__init__(
            name="message",
            description="Send a message",
            aliases=["msg"],
        )

    @staticmethod
    async def execute(ctx, *, content: str):
        await ctx.send(content)

    def get_handler(self):
        async def handler(ctx, *, content: str):
            if not self.enabled:
                await ctx.send(f"❌ {self.name} is disabled")
                return
            await self.execute(ctx, content=content)

        return handler