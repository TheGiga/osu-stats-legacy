
"""
By gigabit- AKA https://github.com/TheGiga 24.03.2022
Glory to Ukraine.
"""

import os

import discord
from dotenv import load_dotenv

from lib import OsuBot, Api, UserNotFound

load_dotenv()
intents = discord.Intents.all()

bot_instance = OsuBot(intents=intents)
API = Api(api_key=os.getenv("API_KEY"))


@bot_instance.event
async def on_ready():
    print("Bot is running...")


@bot_instance.command(name='player')
async def osu_player(
        ctx, *, name: str
):
    try:
        player = await API.get_osu_player(name=name)
    except UserNotFound:
        return await ctx.respond(
            embed=discord.Embed(title="User not found!", colour=discord.Colour.red()),
            ephemeral=True
        )

    embed = discord.Embed(
        title=f'{player.username} - Lvl. {player.level}',
        timestamp=discord.utils.utcnow(),
        description=f"""
            Showing only __RANKED__ statistics.
            
            **PP:** **`{player.pp}`**
            **Rank:** `{player.rank}` | `{player.country_rank}` :flag_{player.country.lower()}:
            **Accuracy**: `{player.accuracy}%`
            
            **SS** count: `{player.total_ss}`
            **S** count: `{player.total_s}`
            
            Player country is **{player.country}** :flag_{player.country.lower()}:
            
            [Go to website profile](https://osu.ppy.sh/users/{player.user_id})
        """,
        colour=discord.Colour.purple()
    )

    embed.set_thumbnail(url=player.profile_image_url)
    embed.set_footer(text=f'ID: {player.user_id}')

    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot_instance.run(os.getenv("TOKEN"))
