import os
from bot import bot
import loader
from commands.help import CustomHelpCommand

#overwrite help command
bot.help_command = CustomHelpCommand()

loader.load_client_credentials()
commands_list = loader.load_commands()
events_list = loader.load_events()

for cmd in commands_list:
    handler = cmd.get_handler()
    bot.command(name=cmd.name,
                aliases=cmd.aliases,
                brief=cmd.brief_description,
                help=cmd.extended_description,
                cooldown=cmd.cooldown,
                extras={'arguments': cmd.arguments_description})(handler)

for evt in events_list:
    handler = evt.get_handler()
    bot.add_listener(handler, f"on_{evt.name}")

bot.run(os.getenv("client_bot"))