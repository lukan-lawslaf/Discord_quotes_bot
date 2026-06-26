import os
import discord
import requests
import json
import random
from keep_alive import keep_alive
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")  # Load the token from the .env file

# Define intents (required for reading messages)
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Needed to read message text

client = discord.Client(intents=intents)

# Sad words and encouragements
sad_words = ["sad", "depressed", "unhappy", "miserable", "angry", "tired"]
starter_encouragements = [
    "😊 Cheer up!",
    "💪 Hang in there.",
    "🌟 You're doing great!",
    "🚀 Keep pushing forward!"
]

# Custom motivational quotes
custom_quotes = [
    "🔥 Push yourself, because no one else is going to do it for you.",
    "🌧️ The hard days are what make you stronger.",
    "🚫 Great things never come from comfort zones.",
    "💖 Believe in yourself, and you will be unstoppable.",
    "⏳ Pain is temporary. Quitting lasts forever.",
    "🎯 Fall seven times, stand up eight.",
    "🦁 You are braver than you believe.",
    "🧠 Your only limit is your mind.",
    "📅 Make today count.",
    "🙌 You’ve got this!"
]

# Short funny motivational stories
short_stories = [
    "📚 Once, a cat tried to catch a mouse but tripped over a ball. The mouse helped the cat up. They now run a business together. Moral? Life can change with kindness.",
    "🐢 A turtle wanted to fly. Birds laughed. He built a paper plane, crashed, but became famous on TurtleTok. Keep dreaming!",
    "🐌 A snail entered a marathon. Took him 3 days, but he finished. He’s now a legend in the snail world. Go at your pace!",
    "🐶 Once a lazy dog decided to exercise and accidentally became a fitness influencer. Moral? Start, even if you're clueless.",
    "🐄 A cow wrote a motivational book called 'Moo-tivation'. It became a bestseller. Start with what you have!"
]

# Random joke list
jokes = [
    "😂 Why don’t scientists trust atoms? Because they make up everything!",
    "😅 I told my computer I needed a break, and now it won’t stop sending me vacation ads.",
    "💀 Why don’t skeletons fight each other? They don’t have the guts.",
    "📖 Why did the math book look sad? Because it had too many problems.",
    "🍬 What do you call a bear with no teeth? A gummy bear!"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    return json_data[0]['q'] + " —" + json_data[0]['a']

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg.startswith("!inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    elif msg.startswith("!motivate"):
        await message.channel.send(random.choice(custom_quotes))

    elif msg.startswith("!joke"):
        await message.channel.send(random.choice(jokes))

    elif msg.startswith("!story"):
        await message.channel.send(random.choice(short_stories))

    elif msg.startswith("!help"):
        help_msg = (
            "**🤖 Motivator Bot Commands:**\n\n"
            "🧠 `!inspire` - Get a wise inspirational quote\n"
            "🔥 `!motivate` - Hear a fiery motivational line\n"
            "😂 `!joke` - Lighten up with a funny joke\n"
            "📖 `!story` - Read a short funny motivational story\n"
            "📸 `!image` - View a motivational crocodile image 🐊\n"
            "🆘 `!help` - See this help message again"
        )
        await message.channel.send(help_msg)

    elif msg.startswith("!image"):
        await message.channel.send(
            "If you think your life is hard, just think about this crocodile's 🐊\nhttps://i.ibb.co/k69kkb0T/crocodile.png"
        )

    elif any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

# Keep alive server
keep_alive()

# ⚠️ Replace this with your bot token if not using .env
client.run(TOKEN)

