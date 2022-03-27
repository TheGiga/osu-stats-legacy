from abc import ABC

import discord


class OsuBot(discord.Bot, ABC):

    """
        Here we can put custom bot methods and properties.
    """

    def __init__(self, *args, **options):
        super().__init__(*args, **options)
