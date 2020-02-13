import random
import time
from Utils import max_retries, bad_return_code


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    try:
        guess_from_user = int(input("Please guess and write a number between 1 to {}: ".format(difficulty)))
        return False, guess_from_user
    except ValueError as e:
        print("Exit code " + str(bad_return_code))
        print("You didn't put a number..", e)
        return True, None
    except:
        print("Exit code " + str(bad_return_code))
        print("\nSomething went wrong...")
        return True, None


def compare_results(secret_num, user_guess, difficulty):
    try:
        while 1 <= user_guess <= difficulty:
            if user_guess == secret_num:
                return False
            else:
                print("So close, but not close enough...")
                return True
        else:
            print("You are not even close!")
            return True
    except:
        print("Exit code " + str(bad_return_code))
        print("\nSomething went wrong...")
        return True


def main_game(difficulty):
    secret_num = generate_number(difficulty)
    user_check, user_guess = get_guess_from_user(difficulty)
    if not user_check:
        user_answer = compare_results(secret_num, user_guess, difficulty)
        if not user_answer:
            print("The number was: " + str(secret_num), "Your guess is correct!\nYou won!\nGoodBay!")
            time.sleep(3)
            return True
        else:
            print("Your wrong!\n")
            user_answer = None
            return False
    else:
        return False


def play(difficulty):
    print("Hello and welcome to Guess Game!\n"
          "In this game you need to guess a number between 1 to the difficulty you choose\n"
          "Let's start!")
    end_game = max_retries(main_game, difficulty=difficulty)
    if end_game:
        return True
    else:
        return False
