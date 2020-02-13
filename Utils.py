import os
import os.path
import time
import urllib.request
import json

scores_file_name = "Scores.txt"
bad_return_code = 1


def range_validator(start, end, var_to_check):
    if start <= var_to_check <= end:
        return True
    else:
        return False


def play_games(number, game, difficulty, function):
    if game == number:
        screen_cleaner()
        end_game = function.play(difficulty)
        return end_game


def max_retries(function, max_tries=3, difficulty=None):
    loading_func = False
    if not loading_func:
        for i in range(max_tries):
            if difficulty is None:
                loading_func = function()
                if loading_func:
                    return True
                else:
                    print("Try number ", str(int(i) + 1), "\n")
                    time.sleep(2)
                    screen_cleaner()
                    loading_func = False
            else:
                loading_func = function(difficulty)
                if loading_func:
                    return True
                else:
                    print("Try number ", str(int(i) + 1), "\n")
                    time.sleep(2)
                    screen_cleaner()
                    loading_func = False
        else:
            print("You've reached maximum retries!\nExiting...", "\n")
            time.sleep(3)
            loading_func = True
            exit()


def game_loader(func1, func2):
    game_valid = max_retries(func1)
    if game_valid:
        time.sleep(2)
        screen_cleaner()
        end_game = max_retries(func2)
        if end_game:
            exit()
        else:
            print("")
    else:
        print("")


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def current_currency_rate():
    api_url = r'https://free.currencyconverterapi.com/api/v5/convert?q=USD_ILS&compact=n&apiKey=4e271815d1893a42cf0b'
    with urllib.request.urlopen(api_url) as url:
        data = json.load(url)
        results = data['results']
        usd_ils = results['USD_ILS']
        currency = float(usd_ils['val'])
        return currency
