from dataclasses import dataclass, field
from typing import Optional, Callable


@dataclass
class Command:
    name: str
    description: str = ""
    aliases: list[str] = field(default_factory=list)
    enabled: bool = True
    cooldown: Optional[float] = None

    def get_handler(self) -> Callable:
        raise NotImplementedError(f"{self.__class__.__name__} must implement get_handler()")

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False