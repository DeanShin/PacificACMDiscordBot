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


class Jeopardy(commands.Cog, name="jeopardy-slash"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="showgrid",
        description="Show the Jeopardy Grid."
    )
    @checks.not_blacklisted()
    async def showgrid(self, interaction: ApplicationCommandInteraction):
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
