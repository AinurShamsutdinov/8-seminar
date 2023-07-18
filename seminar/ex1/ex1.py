# Задание No1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

import json


def data_to_json(file_name: str):
    dict_names = dict()
    with open(file_name, 'r+', encoding='utf-8') as file_read:
        list_names = list(file_read)
    for item in list_names:
        data = item.split('\t')
        dict_names[data[0].capitalize()] = data[1].replace('\n', '')
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(dict_names, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    data_to_json('result.txt')
