import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands
from helpers import checks

import asyncio
import random
import yaml
from enum import Enum, auto

from jeopardy import Board, Game, Team


class BotState(Enum):
    SETUP = auto()
    SELECTION = auto()
    QUESTION = auto()


class Jeopardy(commands.Cog, name="jeopardy-slash"):
    def __init__(self, bot):
        self.bot = bot
        self.stateLock = asyncio.Lock()
        self.commandLock = asyncio.Lock()
        self.state = BotState(1)
        self.game = None

    @commands.slash_command(
        name="loadyaml",
        description="load the yaml file.",
        guild_ids=[275848347175354369]
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
        guild_ids=[275848347175354369]
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

    @commands.slash_command(
        name="initgame",
        description="Initialize the Jeopardy Game.",
        guild_ids=[275848347175354369]
    )
    @checks.not_blacklisted()
    async def initgame(self, interaction: ApplicationCommandInteraction):
        # TODO: initialize board based on yml file.
        def intialize_boards() -> [Board]:
            return []

        self.game = Game(intialize_boards())

        await interaction.send(content="Successfully initialized a game of Jeopardy. Add teams using /addteam!")

    @commands.slash_command(
        name="addteam",
        description="Add a team to the current Jeopardy game.",
        guild_ids=[275848347175354369],
        options=[
            Option(
                name="team_name",
                description="The name of the team you want to add.",
                type=OptionType.string,
                required=True
            )
        ]
    )
    @checks.not_blacklisted()
    async def addteam(self, interaction: ApplicationCommandInteraction, team_name: str):
        if self.game is None:
            raise Exception("No game in progress! Start a game using /initgame first!")

        self.game.add_team(Team(team_name, []))

        await interaction.send(content=f"Successfully created team {team_name}! "
                                       f"Current teams are: {self.game.format_teams()}")

def setup(bot):
    bot.add_cog(Jeopardy(bot))
