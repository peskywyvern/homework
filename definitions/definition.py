import requests


def get_definition(word: str):
    result = requests.get(f'http://api.urbandictionary.com/'
                          f'v0/define?term={word}').json()
    with open('definitions.txt', 'a') as file:
        file.write(f'{word.capitalize()}: \n')
        for i, definition in enumerate(result['list'], start=1):
            file.write(f'{i}. '
                       f'{definition["definition"].replace("[", "").replace("]", "")} \n')


get_definition('life')
