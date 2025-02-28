from typing import Final
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# prendre le token dans un endroit safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Etape 1 : setup le bot
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# Etape 2: Les messages
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("""Le message est vide psq intents n'est pas bien activé""")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# Etape 3 : s'occupper de l'allumage du bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} est allumé')


# Etape 4: S'occupper des message qui arrivent
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Entrée de base
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()