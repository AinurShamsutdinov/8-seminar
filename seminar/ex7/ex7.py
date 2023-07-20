# Задание No7
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.
import pickle


def print_pickle(name_pickle):
    with open(name_pickle, 'rb') as f:
        new_dict = pickle.load(f)
    pickle_str = pickle.dumps(new_dict)
    print(f'{pickle_str = }')


if __name__ == "__main__":
    print_pickle('users.pickle')
