with open('main.py') as m, open('emojies.py') as i, open('emojiPy', 'w') as o:
    o.write(m.read().replace('from emojies import emojies', i.read()))
