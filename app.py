import os
import importlib
from pathlib import Path
from dotenv import load_dotenv
from bot import bot

load_dotenv("credentials/client.secrets")

import os
import importlib
from pathlib import Path
from dotenv import load_dotenv
from bot import bot

load_dotenv("credentials/client.secrets")

base_dir = Path(__file__).parent

# Load all command modules
for file in (base_dir / "commands").glob("*.py"):
    if file.name != "__init__.py":
        importlib.import_module(f"commands.{file.stem}")

# Load all event modules
for file in (base_dir / "events").glob("*.py"):
    if file.name != "__init__.py":
        importlib.import_module(f"events.{file.stem}")

bot.run(os.getenv("client_bot"))