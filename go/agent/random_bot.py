import random
from go.agent.base import Agent
from go.agent.helpers import is_point_an_eye
from go.goboard import Move
from go.gotypes import Point

__all__ = ['RandomBot']


class RandomBot(Agent):
    def select_move(self, game_state):
        """Choose a random valid move that preserves our own eyes."""
        pass
