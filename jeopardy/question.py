from enum import Enum, auto

class QuestionType(Enum):
    NORMAL = auto()
    DAILY_DOUBLE = auto()

class Question:
    def __init__(self, question: str, answer: str, question_type: QuestionType, value: int):
        self._question = question
        self._answer = answer
        self._question_type = question_type
        self._value = value

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    @property
    def question_type(self):
        return self._question_type

    @property
    def value(self):
        return self._value

    @question.setter
    def question(self, value):
        self._question = value

    @answer.setter
    def answer(self, value):
        self._answer = value

    @question_type.setter
    def question_type(self, value):
        self._question_type = value

    @value.setter
    def value(self, value):
        self._value = value
