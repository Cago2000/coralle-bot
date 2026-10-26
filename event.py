from dataclasses import dataclass
from typing import Callable

@dataclass
class Event:
    name: str
    description: str = ""
    enabled: bool = True

    def get_handler(self) -> Callable:
        raise NotImplementedError(f"{self.__class__.__name__} must implement get_handler()")

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False