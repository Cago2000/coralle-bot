from pathlib import Path
from commands.calculator import Calculator
from commands.dice import Dice
from commands.help import Help
from commands.message import Message

base_dir = Path(__file__).parent
command_register_blacklist = ["help"]

command_subclass_mapping = {
    "help": Help(),
    "calculator": Calculator(),
    "dice": Dice(),
    "message": Message(),
}
