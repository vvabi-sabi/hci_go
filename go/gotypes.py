__all__ = [
    'Player',
    'Point',
]


class Player:

    def __init__(self, color):
        pass

    @property
    def other(self):
        '''
        Returns: Player
        '''
        pass


class Point():

    def __init__(self, row, col):
        pass

    def neighbors(self):
        '''
        Returns: list
        '''
        pass

    def __deepcopy__(self, memodict={}):
        # These are very immutable.
        return self

    def __repr__(self):
        return f'Point(row={self.row}, col={self.col})'

    def __hash__(self):
        return (self.row, self.col).__hash__()

    def __eq__(self, other):
        return isinstance(other, Point) and \
               self.row == other.row and self.col == other.col