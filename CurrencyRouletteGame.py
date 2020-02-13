import random
import time
from Utils import current_currency_rate, range_validator, max_retries, bad_return_code


def get_money_interval(difficulty):
    currency = current_currency_rate()
    random_number = random.randint(1, 100)
    total_value = random_number * round(currency, 1)
    interval = ((total_value - (5 - int(difficulty))), (total_value + (5 - int(difficulty))))
    return interval, random_number, total_value


def get_guess_from_user(random_number):
    try:
        guess_from_user = float(input("Please guess what will be the amount in ILS of {} USD: ".format(random_number)))
        return guess_from_user, False
    except ValueError as e:
        print("Exit code " + str(bad_return_code))
        print("You didn't put a number..", e)
        return None, True
    except:
        print("Exit code " + str(bad_return_code))
        print("\nSomething went wrong...")
        return None, True


def main_game(difficulty):
    money_range, random_number, total_value = get_money_interval(difficulty)
    guess_from_user, user_check = get_guess_from_user(random_number)
    if not user_check:
        user_answer = range_validator(int(money_range[0]), int(money_range[1]), int(guess_from_user))
        if user_answer:
            print("The currency is: " + str(total_value), "Your guess is correct!\nYou won!\nGoodBay!")
            time.sleep(3)
            return True
        else:
            print("\nYour wrong!\n")
            return False
    else:
        return False


def play(difficulty):
    print("Hello and welcome to Currency Roulette Game!\n"
          "In this game you will get a random number between 1 to 100 USD and you need to guess the ILS amount\n"
          "Let's start!")
    end_game = max_retries(main_game, difficulty=difficulty)
    if end_game:
        return True
    else:
        return False
