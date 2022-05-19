from jeopardy.team import Team
from jeopardy.board import Board
from disnake import User


class Game:
    def __init__(self, boards: [Board]):
        self._teams = []
        self._boards = boards
        self._turn = 0
        self._board = 0

    def add_team(self, team: Team):
        self._teams.append(team)

    def remove_team(self, team_name: str):
        self._teams = list(filter(lambda team: team.name != team_name, self._teams))

    def format_teams(self):
        "\n---\n".join(self._teams)

    def add_user(self, team_name: str, user: User):
        raise Exception("Unsupported Operation")

    def remove_user(self, user: User):
        raise Exception("Unsupported Operation")

    def print_current_board(self):
        raise Exception("Unsupported Operation")

    def print_question(self, position: str):
        raise Exception('Unsupported Operation')

    def answer_question(self, correct: bool):
        raise Exception("Unsupported Operation")