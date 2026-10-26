from events.base.event import Event


class OnReady(Event):
    def __init__(self):
        super().__init__(
            name="ready",
            description="Bot connected to Discord",
        )

    async def execute(self):
        print("Connected to Discord!")

    def get_handler(self):
        async def handler():
            if not self.enabled:
                return
            await self.execute()

        return handler