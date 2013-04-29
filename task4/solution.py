class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    def __init__(self):
        self.board = {"A": ["", "", ""], "B": ["", "", ""], "C": ["", "", ""]}
        self.turn = 0
        self.order = ["X", "O"]
        self.status = False

    def column(self, position):
        return position[:1]

    def row(self, position):
        return position[1:]

    def __getitem__(self, position):
        column = self.column(position)
        try:
            row = int(self.row(position))
        except ValueError as data:
            raise InvalidKey
        return self.board[column][row - 1]

    def check_for_exception(self, column, row, value):
        if column not in self.board.keys() or row not in (1, 2, 3):
            raise InvalidKey
        elif self.board[column][row-1]:
            raise InvalidMove
        elif value not in ('X', 'O'):
            raise InvalidValue

    def __setitem__(self, position, value):
        column = self.column(position)
        try:
            row = int(self.row(position))
        except ValueError as data:
            raise InvalidKey
        self.check_for_exception(column, row, value)
        if self.turn:
            if self.order[self.turn % 2] == value:
                self.make_move(value, column, row)
            else:
                raise NotYourTurn

        if value != self.order[0]:
            self.order = self.order[::-1]
        self.make_move(value, column, row)

    def __str__(self):
        result_str = '\n'
        for item in (3, 2, 1):
            result_str += '  -------------\n' + str(item)
            for inner_item in ("A", "B", "C"):
                result_str += ' | '
                if self.board[inner_item][item - 1]:
                    result_str += self.board[inner_item][item - 1]
                else:
                    result_str += ' '
            result_str += ' |\n'
        result_str += '  -------------\n    A   B   C  \n'
        return result_str

    def is_winner(self, column, row, player):
        d1 = {"A": 0, "B": 1, "C": 2}
        d2 = {"A": 2, "B": 1, "C": 0}
        if self.turn < 5:
            return False
        if (self.board[column].count(player) == 3):
            return True
        cur_row = [self.board[col][row - 1] for col in self.board.keys()]
        if (cur_row.count(player) == 3):
            return True
        elif d1[column] == row - 1:
            return self.check(d1, row, column, player)
        elif d2[column] == row - 1:
            return self.check(d2, row, column, player)
        else:
            return False

    def update_status(self, player, column, row):
        if self.status:
            return
        elif self.is_winner(column, row, player):
            self.status = player + " wins!"
        elif self.turn == 9:
            self.status = "Draw!"

    def game_status(self):
        if self.status:
            return self.status
        return "Game in progress."

    def make_move(self, value, column, row):
        self.board[column][row - 1] = value
        self.turn += 1
        self.update_status(value, column, row)

    def check(self, d, row, col, player):
        diag = [self.board[col][d[col]] for col in d.keys()]
        if diag.count(player) == 3:
            return True
