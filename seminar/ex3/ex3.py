# Задание No3
# 📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import json
import csv


def json_to_csv():
    user_list: list
    with (open('users.json', 'r', encoding='utf-8') as f,
            open('users.csv', 'w', newline='', encoding='utf-8') as f_write):
        user_list = json.load(f)
        csv_write = csv.writer(f_write, dialect='excel', delimiter=';')
        user_list_csv = list()
        for i, line in enumerate(user_list):
            if i == 0:
                head = ['id', 'name', 'access_level']
                csv_write.writerow(head)
            id_user = list(line.keys())[0]
            print(f'{id_user = }')
            name = line.get(id_user)
            access_lvl = line.get('access_lvl')
            list_wrt = [id_user, name, access_lvl]
            user_list_csv.append(list_wrt)
        csv_write.writerows(user_list_csv)


if __name__ == "__main__":
    json_to_csv()
