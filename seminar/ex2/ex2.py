# Задание No2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
from json import JSONDecodeError

ACCESS_LOW = 1
ACCESS_HIGH = 7


def input_data():
    is_id_unique = True
    is_access_level_ok = False
    user_list = list()
    while True:
        # read from file
        try:
            with open('users.json', 'r+', encoding='utf-8') as f:
                user_list = json.load(f)
        except Exception:
            print("Records are empty.")

        # check if id is unique
        name, id_user, access_lvl = input('Enter name, ID, access_lvl: ').split()
        access_lvl = int(access_lvl)
        set_ids = set()
        for user in user_list:
            if id_user in user.keys():
                is_id_unique = False
                print('Id is not unique')
                break
        # check if access level is between allowed level
        if not ACCESS_LOW <= access_lvl <= ACCESS_HIGH:
            is_access_level_ok = False
            print('Access level should be between 1 and 7')
        else:
            new_user = {id_user: name, 'access_lvl': access_lvl}
            user_list.append(new_user)
            is_access_level_ok = True

        # write to file
        if is_id_unique and is_access_level_ok:
            with open('users.json', 'w') as f:
                json.dump(user_list, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    input_data()
