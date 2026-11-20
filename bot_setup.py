"""Configure the tutorial demos without connecting during import."""

import os
from pathlib import Path

import discord
from dotenv import load_dotenv


def message_intents():
    intents = discord.Intents.default()
    intents.message_content = True
    return intents


def run_demo(client):
    load_dotenv(Path(__file__).with_name('.env'))
    token = os.environ.get('TUTORIAL_BOT_TOKEN', '').strip()
    if not token:
        raise SystemExit('Set TUTORIAL_BOT_TOKEN in .env before starting the bot.')
    client.run(token)
