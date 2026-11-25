# Discord Bot Tutorials

Five standalone Python examples that build up a Discord bot from message events to reactions, role assignment, commands, and embedded help. The moderation example limits message purges and checks permissions. [Start with message events](01_on_message.py) · [Command example](04_commands.py)

## Run locally

Install the project dependencies in a Python virtual environment.

    python -m pip install -r requirements.txt

Copy [.env.example](.env.example) to .env and set TUTORIAL_BOT_TOKEN to your
bot token. Keep .env private. In the Discord Developer Portal, enable the
Message Content intent for the message and command examples. The reaction
roles example needs Server Members intent and a configured target message
and roles. [Gateway intents guide](https://discordpy.readthedocs.io/en/stable/intents.html)

Run one example at a time.

    python 01_on_message.py

For the command demos, !clear accepts a count from 1 to 100. It requires
Manage Messages for the caller and Manage Messages and Read Message History
for the bot.
