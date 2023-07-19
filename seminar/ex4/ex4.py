# Задание No4
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import json


def json_to_csv(read_csv, write_json):
    user_list: list
    with (open(write_json, 'r+', encoding='utf-8') as f_write,
            open(read_csv, 'r', newline='', encoding='utf-8') as f_read):
        csv_read = csv.reader(f_read, dialect='excel', delimiter=';')
        user_list_json = list()
        for i, line in enumerate(csv_read):
            if i != 0:
                row_dict = dict()
                id_user = line[0]
                str().capitalize()
                name = line[1].capitalize()
                hash_sum = 32 + name.__hash__() + id_user.__hash__()
                access_lvl = line[2]
                row_dict['id'] = id_user
                row_dict['name'] = name
                row_dict['hash'] = hash_sum
                row_dict['access_lvl'] = access_lvl
                user_list_json.append(row_dict)
        json.dump(user_list_json, f_write, indent=2)


if __name__ == "__main__":
    json_to_csv('users.csv', 'users.json')
