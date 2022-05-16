from team import Team
from board import Board
from disnake import User


class Game:
    def __init__(self, teams: [Team], boards: [Board]):
        self._teams = teams
        self._boards = boards
        self._turn = 0
        self._board = 0

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