from commands.base.command import Command


class Message(Command):
    def __init__(self):
        super().__init__(
            name="message",
            brief_description="Repeats your message",
            extended_description="Repeats your message",
            aliases=["msg"],
            arguments_description=
            {
                "content": "Text after command call"
            },
        )

    @staticmethod
    async def execute(ctx, *, content: str):
        await ctx.send(content)

    def get_handler(self):
        async def handler(ctx, *, content: str):
            if not self.enabled:
                await ctx.send(f"{self.name} is disabled")
                return
            await self.execute(ctx, content=content)
        return handler