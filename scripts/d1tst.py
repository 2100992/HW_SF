from configparser import ConfigParser
import trello


def get_config(path):
    config = ConfigParser()
    config.read(path)
    return config


config = get_config('trello.conf')

api_key = config['trello']['api_key']
token = config['trello']['token']
b1_id = config['trello']['b1_id']
b2_id = config['trello']['b2_id']


def main():
    print(f'api_key = {api_key}')
    print(f'token = {token}')

    TA = trello.TrelloApi(api_key, token)

    for column in TA.boards.get_list(b1_id):
        print(column['name'])

    print()

    for column in TA.boards.get_list(b2_id):
        print(column['name'])
        if "Готово" in column['name']:
            list_id = column['id']
            card = newCard(TA, 'Модуль C4', list_id)
            print('new card')
            print(card)
            for card in TA.lists.get_card(list_id):
                print(card['name'])


def newCard(TA, description, list_id):
    card = TA.cards.new(description, list_id)
    return card


if __name__ == "__main__":
    main()
