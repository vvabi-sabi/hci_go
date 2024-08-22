import copy
from go.gotypes import Player
from go.gotypes import Point
from go.scoring import compute_game_result

__all__ = [
    'Board',
    'GameState',
    'Move',
]


class IllegalMoveError(Exception):
    pass


class GoString():  # <1>

    def __init__(self, color, stones, liberties):
        pass

    def remove_liberty(self, point):
        pass

    def add_liberty(self, point):
        pass

    def merged_with(self, go_string):  # <2>
        assert go_string.color == self.color
        pass

    @property
    def num_liberties(self):
        pass

    def __eq__(self, other):
        pass
# <1> Go strings are stones that are linked by a chain of connected stones of the same color.
# <2> Return a new Go string containing all stones in both strings.


class Board():  # <1>

    def __init__(self, num_rows, num_cols):
        pass
# <1> A board is initialized as empty grid with the specified number of rows and columns.

    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
# <1> First, we examine direct neighbors of this point.

# <2> Merge any adjacent strings of the same color.
# <3> Reduce liberties of any adjacent strings of the opposite color.
# <4> If any opposite color strings now have zero liberties, remove them.

# <5> Removing a string can create liberties for other strings.

# <6> Returns the content of a point on the board:  a Player if there is a stone on that point or else None.
# <7> Returns the entire string of stones at a point: a GoString if there is a stone on that point or else None.
        pass

    def __eq__(self, other):
        pass


class Move():  # <1>

    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        pass

    @classmethod
    def play(cls, point):  # <2>
        pass

    @classmethod
    def pass_turn(cls):  # <3>
        pass

    @classmethod
    def resign(cls):  # <4>
        pass
# <1> Any action a player can play on a turn, either is_play, is_pass or is_resign will be set.
# <2> This move places a stone on the board.
# <3> This move passes.
# <4> This move resigns the current game


class GameState():

    def __init__(self, board, next_player, previous, move):
        pass

    def apply_move(self, move):  # <1>
        pass

    @classmethod
    def new_game(cls, board_size):
        pass
# <1> Return the new GameState after applying the move.

    def is_move_self_capture(self, player, move):
        pass

    @property
    def situation(self):
        pass

    def does_move_violate_ko(self, player, move):
        pass

    def is_valid_move(self, move):
        pass

    def is_over(self):
        pass

    def legal_moves(self):
        pass

    def winner(self):
        pass
