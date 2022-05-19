from disnake import User


class Team:
    def __init__(self, name: str, users: [User] = None, points: int = 0):
        if users is None:
            users = []
        self._name = name
        self._users = users
        self._points = points

    @property
    def name(self):
        return self._name

    @property
    def users(self):
        return self._users

    @property
    def points(self):
        return self._points

    @name.setter
    def name(self, value):
        self._name = value

    @users.setter
    def users(self, value):
        self._users = value

    @points.setter
    def points(self, value):
        self._points = value

    def __str__(self):
        endl = "\n"
        return f'{self._name}{endl}' \
               f'{[f"- {user}{endl}" for user in self.users]}'
