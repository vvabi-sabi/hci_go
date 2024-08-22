from __future__ import print_function
from go.agent.random_bot import RandomBot
from go import goboard
from go.utils import print_board, print_move, point_from_coords
from six.moves import input
import time


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot = RandomBot()

    while not game.is_over():
        print(chr(27) + "[2J")
        print_board(game.board)
        if game.next_player.color == 'black':
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            time.sleep(1)
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)


if __name__ == '__main__':
    main()