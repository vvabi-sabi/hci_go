from go import gotypes

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
    None: ' . ',
    'black': ' x ',
    'white': ' o ',
}


def print_move(player, move):
    ''' for example:
    >>> black B2
    >>> white C9
    '''
    pass


def print_board(board):
    ''' for example:
    9  .  .  o  .  .  .  .  .  .
    8  .  .  .  .  .  .  .  .  .
    7  .  .  .  x  .  .  .  .  .
    6  .  .  .  .  .  .  .  o  .
    5  x  .  .  .  x  .  x  .  .
    4  .  .  o  .  .  .  x  .  .
    3  .  .  o  .  .  .  .  x  .
    2  .  .  .  .  .  o  .  o  .
    1  .  .  .  .  .  .  .  .  .
        A  B  C  D  E  F  G  H  J
    '''
    pass


def point_from_coords(coords):
    '''
    human coordinates to point:
    "B2" -> Point(2,2)
    Returns: Point
    '''
    pass

def coords_from_point(point):
    '''
    Point(2,3) -> "C2"
    Returns: str
    '''
    pass

