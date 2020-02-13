from Utils import scores_file_name
import json


def add_score(difficulty, name):
    if name != "" and "\n":
        points_of_winning = (difficulty * 3) + 5
        try:
            score_file_r = eval(open(scores_file_name, "r+").read())
            if name in score_file_r.keys():
                new_score = int(points_of_winning) + int(score_file_r[name])
                handle_file(scores_file_name, new_score, name)
            else:
                handle_file(scores_file_name, points_of_winning, name)
        except FileNotFoundError or SyntaxError:
            handle_file(scores_file_name, points_of_winning, name)
    else:
        print("You must have name!")


def handle_file(file, score, user_name):
    try:
        file_dict = eval(open(file, "r+").read())
        try:
            file_dict.pop(user_name)
            file_dict[user_name] = score
            write_dict_to_file(file, file_dict)
        except KeyError:
            file_dict[user_name] = score
            write_dict_to_file(file, file_dict)
    except FileNotFoundError or SyntaxError:
        new_file_dict = {user_name: score}
        write_dict_to_file(file, new_file_dict)


def write_dict_to_file(file, dictionary):
    file_to_write = open(file, "w+")
    file_to_write.write(json.dumps(dictionary))
    file_to_write.close()
