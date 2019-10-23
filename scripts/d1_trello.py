import requests
from configparser import ConfigParser
import sys

def get_config(path):
    config = ConfigParser()
    config.read(path)
    return config


def read(url, board_id, auth_params):
    column_data = requests.get(url.format(
        'boards') + '/' + board_id + '/lists', params=auth_params).json()

    for column in column_data:
        print(column['name'])
        task_data = requests.get(url.format(
            'lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        if not task_data:
            print('\t' + 'Нет задач!')
            continue
        for task in task_data:
            print('\t' + task['name'])

def create(name, column_name, url, board_id, auth_params):
    column_data = requests.get(url.format(
        'boards') + '/' + board_id + '/lists', params=auth_params).json()
    
    for column in column_data:
        if column['name'] == column_name:
            requests.post(url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})
            break

def move(name, column_name, url, board_id, auth_params):
    column_data = requests.get(url.format(
        'boards') + '/' + board_id + '/lists', params=auth_params).json()
# 
# 
# ДОПИСАТЬ!!!!!!!!!!!!!!!!!!!
# 
#         
#     


def main():
    config = get_config('trello.conf')

    auth_params = {
        'key': config['trello']['api_key'],
        'token': config['trello']['token'],
    }

    base_url = config['trello']['base_url']
    b1_id = config['trello']['b1_id']
    b2_id = config['trello']['b2_id']

    

    if len(sys.argv) <= 2:
        read(base_url, b2_id, auth_params)
    else:
        create(sys.argv[1], sys.argv[2], base_url, b2_id, auth_params)


if __name__ == "__main__":
    main()
