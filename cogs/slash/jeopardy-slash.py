import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands

from helpers import checks

# class JeopardyGridRow(disnake.ui.ActionRow):
#     def __init__(self):
#         super().__init__()
#         self.add_button(label="option1")
#         self.add_button(label="option2")
#         self.add_button(label="option3")
#         self.add_button(label="option4")
#         self.add_button(label="option5")

# class JeopardyGrid(disnake.ui.View):
#     def __init__(self):
#         super().__init__()
#         self.add_item(JeopardyGridRow())

import asyncio
import random
import yaml
from enum import Enum, auto

class BotState(Enum):
    SETUP = auto()
    SELECTION = auto()
    QUESTION = auto()


class Jeopardy(commands.Cog, name="jeopardy-slash"):
    def __init__(self, bot):
        self.bot = bot
        self.stateLock = asyncio.Lock()
        self.commandLock = asyncio.Lock()
        self.state =  BotState(1)

        



    @commands.slash_command(
        name="loadyaml",
        description="load the yaml file.",
        guild_ids=[250465040921133057] 
    )
    @checks.not_blacklisted()
    async def loadyaml(self, interaction: ApplicationCommandInteraction):

        #load in board data
        stream = open("ymls/catagories.yml", "r") 
        catagories = yaml.load(stream)

        stream = open("ymls/questions.yml", "r")
        questions = yaml.load(stream)

        print(repr(questions))

        stream = open("ymls/answers.yml", "r")
        answers = yaml.load(stream)

        embed = disnake.Embed(
            title="yamls loaded",
            description=f"All files were read in successfully",
            color=0x9C84EF
        )

        await interaction.send(embed=embed)

    @commands.slash_command(
        name="showgrid",
        description="Show the Jeopardy Grid.",
        guild_ids=[250465040921133057]
    )
    @checks.not_blacklisted()
    async def showgrid(self, interaction: ApplicationCommandInteraction):
        #async example
        async with self.stateLock:
            self.cState = random.choice(list(BotState))




        row = disnake.ui.ActionRow()
        row.add_button(label="option1")
        row.add_button(label="option2")
        row.add_button(label="option3")
        row.add_button(label="option4")
        row.add_button(label="option5")
        embed = disnake.Embed(
            description="Grid of options",
            color=0x9C84EF
        )
        await interaction.send(embed=embed, components=row)


def setup(bot):
    bot.add_cog(Jeopardy(bot))
