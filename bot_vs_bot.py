from go.agent.random_bot import RandomBot
from go import goboard
from go.utils import print_board, print_move
import time


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        'black': RandomBot(),
        'white': RandomBot(),
    }
    while not game.is_over():
        time.sleep(0.9)  # <1>

        print(chr(27) + "[2J")  # <2>
        print_board(game.board)
        bot_move = bots[game.next_player.color].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()

# <1> We set a sleep timer to 0.9 seconds so that bot moves aren't printed too fast to observe
# <2> Before each move we clear the screen. This way the board is always printed to the same position on the command line.