import types
from actions.exceptions import InvalidException, GracefulExit
from actions.game import Game
from actions.input import get_user_input, get_computer_input
from models.entity import EntityEnum


def main():
    print("enter [q]uit to leave")

    game = Game()
    while True:
        game.print_help()
        try:
            user_action = get_user_input()
            if isinstance(user_action, types.FunctionType):
                user_action()
        except InvalidException:
            print("Wrong Input, please follow instructions")
            continue
        except GracefulExit:
            print("Good-bye")
            break
        if not isinstance(user_action, EntityEnum):
            continue

        com = get_computer_input()
        winner = game.calculate_winner(user_action, com)
        game.add_game()
        print(f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Game No. {game.game_number}
        User: {user_action.name}, Computer: {com.name}
        -> Winner: {winner.name}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")


if __name__ == '__main__':
    main()
