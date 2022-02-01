from urllib.request import urlopen
from json import loads


def e2u(x):
    return f'{x!a}'[1:-1]


if __name__ == '__main__':
    with urlopen('https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json') as response:
        emojies = loads(response.read().decode())

    result = ['emojies = {']
    for e in emojies:
        u = ''.join(map(e2u, e['emoji']))
        for a in e['aliases']:
            result.append(f'    ":{a}:": "{u}",')
    result.append('}')

    with open('emojies.py', 'w') as f:
        f.write('\n'.join(result))
