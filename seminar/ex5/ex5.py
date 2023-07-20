# Задание No5
# 📌 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их
# содержимое в виде одноимённых pickle файлов.
import json
import os
import pickle


def json_file_to_pikle(file_name):
    pickle_name = file_name.split('.')[0] + '.pickle'
    with (open(file_name, 'r', encoding='utf-8') as f_read,
            open(pickle_name, 'wb') as f_write):
        user_list = json.load(f_read)
        pickle.dump(user_list, f_write)


def read_pickle():
    with open('users.pickle', 'rb') as f_read:
        new_dict = pickle.load(f_read)
        print(f'{new_dict = }')


if __name__ == "__main__":
    list_files = os.listdir()
    list_json_files: list = list()
    for file in list_files:
        if file.endswith('json'):
            json_file_to_pikle(file)
    read_pickle()
