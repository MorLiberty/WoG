import time
import random
from Utils import screen_cleaner, max_retries, bad_return_code


def generate_sequence(difficulty):
    generated_list = []
    for num in range(1, int(difficulty) + 1):
        generated_list.append(random.randint(1, 101))
    return generated_list


def get_list_from_user(difficulty):
    try:
        list_from_user = []
        for i in range(1, int(difficulty) + 1):
            number_from_user = int(input("Please enter guessed number " + str(i) + ": "))
            list_from_user.append(number_from_user)
        print("This is your list: " + str(list_from_user))
        return False, list_from_user
    except ValueError as e:
        print("Exit code " + str(bad_return_code))
        print("You must enter a number to the list!", e)
        list_from_user = []
        return True, None
    except:
        print("Exit code " + str(bad_return_code))
        print("\nSomething went wrong...")
        return True, None


def is_list_equal(generated_list, list_from_user, difficulty):
    try:
        if generated_list == list_from_user:
            return False
        elif generated_list != list_from_user:
            right_numbers = 0
            for number in range(int(difficulty)):
                if generated_list[number] == list_from_user[number]:
                    right_numbers += 1
                else:
                    print(end="")
            else:
                print("You need to work on your memory...\nYou guessed only " + str(right_numbers) + " number right")
            return True
    except IndexError as e:
        print("Exit code " + str(bad_return_code))
        return True


def main_game(difficulty):
    generated_list = generate_sequence(difficulty)
    for num in range(0, int(difficulty)):
        print("number in place " + str(num + 1) + " is: " + str(generated_list[num]))
        time.sleep(0.7)
        screen_cleaner()
    user_check, user_list = get_list_from_user(difficulty)
    if not user_check:
        user_answer = is_list_equal(generated_list, user_list, difficulty)
        if not user_answer:
            print("Your memory is great! All " + str(difficulty) + " are correct!" + "\nYou Won!\nGoodBay!")
            time.sleep(3)
            return True
    else:
        return False


def play(difficulty):
    print("Hello and welcome to Memory Game!\n"
          "In this game you need to memorize a list of numbers and remember them\n"
          "Pay attention we are about to start in 5 seconds!")
    time.sleep(5)
    screen_cleaner()
    end_game = max_retries(main_game, difficulty=difficulty)
    if end_game:
        return True
    else:
        return False
