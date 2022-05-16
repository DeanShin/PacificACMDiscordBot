from question import Question


class Board:
    def __init__(self, questions: [[Question]], row_values: [], col_categories: []):
        if len(row_values) is not len(questions):
            raise Exception(f"Invalid input: was provided {len(row_values)} row values, but found {len(questions)} "
                            f"rows of questions.")
        elif len(col_categories) is not len(questions[0]):
            raise Exception(f"Invalid input: was provided {len(col_categories)} column categories, but found "
                            f"{len(questions[0])} columns of questions")
        # Code to make Dustin mad
        elif len(set([len(row) for row in questions])) != 1:
            raise Exception(f"Invalid input: questions matrix does has uneven number of rows.")
        self.questions = questions
        self.row_values = row_values
        self.col_categories = col_categories

    def format_board(self) -> str:
        raise Exception("Not implemented yet.")

    def get_question(self, position: str) -> Question:
        raise Exception("Not implemented yet.")

    def consume_question(self, position: str):
        raise Exception("Not implemented yet.")