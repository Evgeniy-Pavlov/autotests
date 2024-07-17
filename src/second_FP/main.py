import os
import json
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type=str, help='Путь до файла со справочником пользователей. Файл должен быть обязательно в формате json', default='users.json')
    parser.add_argument('-b', type=str, help='Путь до файла со списком книг. Файл должен быть обязательно в формате csv', default='./books.csv')
    return parser.parse_args()

def main():
    arg_parse = parse_arguments()
    users_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), arg_parse.u))
    print(arg_parse.u)
    with open(users_file_path, 'r') as f:
        users_dict = json.load(f)
        

if __name__ == '__main__':
    main()