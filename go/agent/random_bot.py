import random
from go.agent.base import Agent
from go.agent.helpers import is_point_an_eye
from go.goboard import Move
from go.gotypes import Point

__all__ = ['RandomBot']


class RandomBot(Agent):
    def select_move(self, game_state):
        '''
        Choose a random valid move that preserves our own eyes.
        Returns: Move.pass_turn() or Move.play(...)
        '''
        # - Initializes an empty list called candidates to store potential valid moves.
		# - Iterates through each point on the board.
		# - For each point, creates a Point object representing the coordinates.
		# - Checks if the move is valid.
		# - Additionally, checks if the candidate point is not an eye for the next player.
		# - If both conditions are met, adds the candidate point to the candidates list.
		# - After checking all points, if no valid candidates are found, it returns a pass.
		# - If there are valid candidates, it randomly selects one from the list of candidates.
        pass
