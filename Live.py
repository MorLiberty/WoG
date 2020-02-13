from Utils import range_validator, play_games, screen_cleaner, bad_return_code
from Score import add_score
import GuessGame
import MemoryGame
import CurrencyRouletteGame


name = ""


def welcome():
    global name
    name = input("Please enter your name: ")
    if not (name.isdigit() or name == "\n"):
        screen_cleaner()
        name = name.upper()
        print("Hello %s and welcome to the World of Games (WoG)!\n"
              "Here you can find many cool games to play.\n" % name)
        return True
    else:
        print("Exit code " + str(bad_return_code))
        print("Your name is not valid!\n")
        return False


def load_game():
    try:
        game = input("Please choose a game to play:\n"
                     "1. Memory Game - A sequence of number will appear for 1 second,\n"
                     "And you have to guess it back\n"
                     "2. Guess Game - Guess a number and see if you chose like the computer\n"
                     "3. Currency Roulette - Try and guess the value of a random amount of USD in ILS\n"
                     "Please write your number here: ")
        game = int(game)
        user_check_game = range_validator(1, 3, game)
        difficulty = input("\nPlease choose game difficulty from 1 to 5: ")
        difficulty = int(difficulty)
        user_check_difficulty = range_validator(1, 5, difficulty)
        user_check = user_check_game and user_check_difficulty
        if user_check:
            end_game1 = play_games(1, game, difficulty, MemoryGame)
            end_game2 = play_games(2, game, difficulty, GuessGame)
            end_game3 = play_games(3, game, difficulty, CurrencyRouletteGame)
            if end_game1 or end_game2 or end_game3:
                add_score(difficulty, name)
                return True
            else:
                return False
        else:
            print("Exit code " + str(bad_return_code))
            print("\nYou didn't put the right numbers!", "\n")
            return False
    except ValueError as e:
        print("Exit code " + str(bad_return_code))
        print("\nYou have to choose numbers!", e, "\n")
        return False
