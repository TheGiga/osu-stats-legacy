
"""
By gigabit- AKA https://github.com/TheGiga 24.03.2022
Glory to Ukraine.
"""

import discord
import os

from lib import OsuBot, Api
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()

bot_instance = OsuBot(intents=intents)
API = Api(api_key=os.getenv("API_KEY"))


@bot_instance.event
async def on_ready():
    print("Bot is running...")


@bot_instance.slash_command(name='player')
async def osu_player(
        ctx: discord.ApplicationContext,
        name: str
):
    player = await API.get_osu_player(name=name)

    embed = discord.Embed(
        title=f'{player.username} - Lvl. {player.level}',
        timestamp=discord.utils.utcnow(),
        description=f"""
            Showing only __RANKED__ statistics.
            
            **PP:** **`{player.pp}`**
            **Rank:** `{player.rank}` | `{player.country_rank}` :flag_{player.country.lower()}:
            **Accuracy**: `{player.accuracy}`%
            
            **SS** count: `{player.total_ss}`
            **S** count: `{player.total_s}`
            
            Player country is **{player.country}** :flag_{player.country.lower()}:
        """,
        colour=discord.Colour.purple()
    )

    embed.set_thumbnail(url=player.profile_image_url)
    embed.set_footer(text=f'ID: {player.user_id}')

    await ctx.respond(embed=embed)


if __name__ == "__main__":
    bot_instance.run(os.getenv("TOKEN"))
