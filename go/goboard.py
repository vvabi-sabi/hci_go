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


class GoString():
	'''
	Go strings are stones that are linked by a chain of connected stones of the same color.
	'''

    def __init__(self, color, stones, liberties):
        pass

    def remove_liberty(self, point):
    	'''
    	Removes a specified point from the set of liberties.
    	'''
        pass

    def add_liberty(self, point):
	    '''
	    Adds a specified point to the set of liberties.
	    '''
        pass

    def merged_with(self, go_string):
    	'''
    	Return a new Go string containing all stones in both strings.
    	'''
        assert go_string.color == self.color # It asserts that both GoString instances have the same color.
		 # - Combines their stones using a union operation.
		 # - Computes a new set of liberties that includes the liberties from both strings
		 # minus any stones that are now part of the merged string.
		 # - Returns a new instance of GoString representing the merged state.
        pass

    @property
    def num_liberties(self):
    	'''
    	A property that returns the number of liberties.
    	'''
        pass

    def __eq__(self, other):
    	'''
    	Checks for equality between two GoString instances.
    	'''
    	# - It checks if other is an instance of GoString.
		# - Compares the color, stones, and liberties attributes of both instances for equality.
		# - Returns True if they are equal, otherwise returns False.
        pass


class Board():  # <1>
	'''
	A board is initialized as empty grid with the specified number of rows and columns.
	'''
    def __init__(self, num_rows, num_cols):
        pass

    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        
        # - Initializes lists to track adjacent stones of the same and opposite color, as well as liberties (empty points).
        # - First, we examine direct neighbors of this point.
        # (Iterates over neighboring points to categorize them as either empty (liberties), same color, or opposite color.)
        	# updating the list of free points (points without stones)
        	# updating the list of adjacent stones of the same color
        	# updating the list of adjacent stones of the opposite color
        # - Creates a new Go string for the player's stone at the specified point.

		# - Merge any adjacent strings of the same color.
		# - Updates the grid with the new string at all points it occupies.
		# - Reduce liberties of any adjacent strings of the opposite color.
		# - If any opposite color strings now have zero liberties, remove them.
		pass

	def _remove_string(self, string):
		'''
		Removes a Go string from the board.
		(Removing a string can create liberties for other strings.)
		'''
		# - Iterates through each point in the string and checks its neighbors.
		# - For each neighbor, if it belongs to a different string, it adds the current point as a liberty for that neighboring string.
		# - Finally, it sets each point of the removed string in _grid to None, effectively removing it from the board.
		pass

	def is_on_grid(self, point):
		'''
		Checks if a given point is within the boundaries of the board.
		'''
    	pass
	
	def get(self, point): 
		'''
		Retrieves the color of the stone at a specified point on the board.
		'''
		pass
	
	 def get_go_string(self, point):
		'''
		Returns the entire string of stones at a point: a GoString if there is a stone on that point or else None.
		'''
        pass

    def __eq__(self, other):
	    '''
	    Compares two board instances for equality.	
	    '''
        pass


class Move():
	'''
	Any action a player can play on a turn, either is_play, is_pass or is_resign will be set.
	'''
	
    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        pass

    @classmethod
    def play(cls, point):
    	'''
    	This move places a stone on the board.
    	'''
        pass

    @classmethod
    def pass_turn(cls):
    	'''
    	This move passes.
    	'''
        pass

    @classmethod
    def resign(cls):
    	'''
    	This move resigns the current game
    	'''
        pass


class GameState():

    def __init__(self, board, next_player, previous, move):
        pass

    def apply_move(self, move):
    	'''
    	Return the new GameState after applying the move.
    	'''
    	# - If the move is a play, it creates a deep copy of the current board and 
    	# places the stone for the next player at the specified point.
		# - If the move is not a play (e.g., a pass), it keeps the current board unchanged.
		# - It then returns a new instance of GameState with the updated board, 
		# switches to the other player, and records the current state as the previous state.
        pass

    @classmethod
    def new_game(cls, board_size):
    	'''
    	Initializes a new game with a specified board size.
    	'''
    	# - It creates a new Board instance with the specified dimensions.
		# - Finally, it returns a new instance of GameState, setting the initial player to 'black' 
		# and both previous state and last move to None.
        pass

    def is_move_self_capture(self, player, move):
    	'''
    	Checks if a given move would result in self-capture for the specified player.
    	'''
    	# - If the move is not a play, it immediately returns False.
		# - It creates a deep copy of the current board and places the player's stone at the specified point of the move.
		# - It retrieves the Go string (group of connected stones) that includes the newly placed stone.
		# - Finally, it checks if this Go string has zero liberties.
        pass

    @property
    def situation(self):
        return (self.next_player, self.board)

    def does_move_violate_ko(self, player, move):
        if not move.is_play:
            return False
        next_board = copy.deepcopy(self.board)
        next_board.place_stone(player, move.point)
        next_situation = (player.other, next_board)
        past_state = self.previous_state
        while past_state is not None:
            if past_state.situation == next_situation:
                return True
            past_state = past_state.previous_state
        return False

    def is_valid_move(self, move):
        if self.is_over():
            return False
        if move.is_pass or move.is_resign:
            return True
        return (
            self.board.get(move.point) is None and
            not self.is_move_self_capture(self.next_player, move) and
            not self.does_move_violate_ko(self.next_player, move))

    def is_over(self):
        if self.last_move is None:
            return False
        if self.last_move.is_resign:
            return True
        second_last_move = self.previous_state.last_move
        if second_last_move is None:
            return False
        return self.last_move.is_pass and second_last_move.is_pass

    def legal_moves(self):
        moves = []
        for row in range(1, self.board.num_rows + 1):
            for col in range(1, self.board.num_cols + 1):
                move = Move.play(Point(row, col))
                if self.is_valid_move(move):
                    moves.append(move)
        # These two moves are always legal.
        moves.append(Move.pass_turn())
        moves.append(Move.resign())
        return moves

    def winner(self):
        if not self.is_over():
            return None
        if self.last_move.is_resign:
            return self.next_player
        game_result = compute_game_result(self)
        return game_result.winner
