from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Command:
    name: str
    description: str = ""
    aliases: list[str] = field(default_factory=list)
    enabled: bool = True
    cooldown: Optional[float] = None

    def execute(self, *args, **kwargs):
        """Execute the command."""
        raise NotImplementedError

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False