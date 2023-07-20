# Задание No6
# 📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import pickle


def csv_file_to_pikle():
    with (open('users.csv', 'r', encoding='utf-8') as f_read,
            open('users.pickle', 'wb') as f_write):
        user_list_csv = csv.reader(f_read, dialect='excel', delimiter=';')
        head_list: list = list()
        users_list_dict = list()
        for i, item in enumerate(user_list_csv):
            if i == 0:
                head_list = list
            record = dict()
            record[head_list[0]] = item[0]
            record[head_list[1]] = item[1]
            record[head_list[2]] = item[2]
            users_list_dict.append(record)
        pickle.dump(users_list_dict, f_write)


if __name__ == "__main__":
    csv_file_to_pikle()
