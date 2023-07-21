# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
#   с учётом всех вложенных файлов и директорий.
# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import csv
import json
import os
import pathlib
import pickle


def return_dir_pathlib(path):
    files = pathlib.Path(path)
    # print(f'{files}')
    directory = list()
    for file in files.rglob('*'):
        files_dict = dict()
        basename = os.path.basename(file)  # parent directory
        parent_path = file.parent.name  # get tail from path
        is_dir = os.path.isdir(file)
        size: int = int()
        if is_dir:
            for path, dirs, files in os.walk(file):
                for f in files:
                    fp = os.path.join(path, f)
                    size += os.path.getsize(fp)
        else:
            size = os.path.getsize(file)
        files_dict['file'] = basename
        files_dict['parent_dir'] = parent_path
        files_dict['is_dir'] = is_dir
        files_dict['size'] = size
        directory.append(files_dict)
        with (open('directory_content.json', 'w', encoding='utf-8') as f_json,
              open('directory_content.csv', 'w', newline='', encoding='utf-8') as f_csv,
              open('directory_content.pickle', 'wb') as f_pickle):
            json.dump(directory, f_json, ensure_ascii=False, indent=2)
            pickle.dump(directory, f_pickle)
            csv_writer = csv.writer(f_csv, dialect='excel', delimiter=';')
            for index, f_item in enumerate(directory):
                if index == 0:
                    head = list(f_item.keys())
                    csv_writer.writerow(head)
                csv_writer.writerow([f_item['file'], f_item['parent_dir'], f_item['is_dir'], f_item['size']])
    return directory


if __name__ == "__main__":
    path = '/Users/ainur/PycharmProjects/8-seminar/seminar'
    list_of_files = return_dir_pathlib(path)
    for item in enumerate(list_of_files):
        print(f'{item}')
