import importlib
import inspect
from pathlib import Path
from dotenv import load_dotenv
import constants
from commands.base.command import Command
from events.base.event import Event

base_dir = constants.base_dir


def load_client_credentials():
    load_dotenv(".credentials/client.secrets")


def iterate_folder(item_dir: Path, ctx_str: str, base_class):
    items = []
    for item in item_dir.glob("*.py"):
        if item.name == "__init__.py":
            continue
        module = importlib.import_module(f"{ctx_str}.{item.stem}")
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, base_class) and obj is not base_class:
                instance = obj()
                items.append(instance)
    return items


def load_commands():
    commands_dir = base_dir / "commands"
    commands = iterate_folder(commands_dir, "commands", Command)
    return commands


def load_events():
    events_dir = base_dir / "events"
    events = iterate_folder(events_dir, "events", Event)
    return events

def load_command_mapping():
    return {
        command.name: command
        for command in load_commands()
    }