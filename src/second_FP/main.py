import os
import csv
import json
import datetime
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type=str, help='Путь до файла со справочником пользователей. Файл должен быть обязательно в формате json', default='users.json')
    parser.add_argument('-b', type=str, help='Путь до файла со списком книг. Файл должен быть обязательно в формате csv', default='./books.csv')
    return parser.parse_args()


def read_json(file_path):
    with open(file_path, 'r') as f:
        users_dict = json.load(f)
    return users_dict


def read_csv(file_path):
    with open(file_path, newline='') as f:
        result = list(csv.DictReader(f))
    return result


def main():
    arg_parse = parse_arguments()
    users_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), arg_parse.u))
    books_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), arg_parse.b))
    list_users = read_json(users_file_path)
    list_books = read_csv(books_file_path)
    for e, book in enumerate(list_books):
        user = list_users[e%len(list_users)]
        if not user.get('books'):
            user['books'] = [book]
        else:
            user['books'].append(book)
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), f'result_{datetime.datetime.now().date()}.json')), "w") as f:
        json.dump(list_users, f)       


if __name__ == '__main__':
    main()