# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
#   с учётом всех вложенных файлов и директорий.
# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
import shutil


def return_dir_content(path):
    files = os.walk(path)
    list_dir = os.listdir(path)
    print(f'{files}')
    directory = list()
    for file in enumerate(files):
        print(f'{file}')
        files_dict = dict()
        cur_path = file[1][0]
        content = file[1][1]
        if len(content) > 0:
            for item in content:
                if
        basename = os.path.basename(cur_path)           # parent directory
        parent_path = os.path.split(cur_path)[0]        # get tail from path
        parent_dir = os.path.split(parent_path)[1]
        is_dir = os.path.isdir(cur_path)
        size: int = int()
        if is_dir:
            for path, dirs, files in os.walk(cur_path):
                for f in files:
                    fp = os.path.join(path, f)
                    size += os.path.getsize(fp)
        else:
            size = os.path.getsize(cur_path)
        print(f'{file = }\t{type(file)}')
        print(f'{basename = }\t{parent_dir = }\t{is_dir = }\t{size = }')
        files_dict['dir'] = basename
        files_dict['parent_dir'] = parent_dir
        files_dict['is_dir'] = is_dir
        files_dict['size'] = size
        directory.append(files_dict)
    print(f'{directory}')


if __name__ == "__main__":
    path = '/Users/ainur/PycharmProjects/8-seminar/seminar'
    return_dir_content(path)

