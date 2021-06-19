from paji.command.domain import helpers


class ConsoleHelper(helpers.ConsoleHelperBase):

    def print(self, message: str):
        print(message)
