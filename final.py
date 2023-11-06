from difflib import get_close_matches
import json


def translate(word):
    global data
    if word in data:
        print('-' * 20)
        print('Translate : ')
        print(data[word]['translate'])
        print('-' * 20)
        print('Examples : ')
        for ex in data[word]['examples']:
            print('=> ', ex)
        print('-' * 20)


data = json.load(open('words.json', encoding='utf-8'))

print('\n')
print('=========== Hi ===========')
print('\n')

word = input('search a word : ')
alternate = get_close_matches(word, data.keys())

if word in data:
    translate(word)
elif len(alternate) > 0:
    check = input("Did you mean %s ? y/n : " % alternate[0])
    if check in ['Y', 'y']:
        translate(alternate[0])
    elif check in ['N', 'n']:
        print('--- bye ---')
    else:
        print('--- wrong input ---')
else:
    print('--- word not found ---')
    check = input('Should I add this word?  y/n : ')
    examples = []
    example = ''
    if check in ['Y', 'y']:
        meaning = input('Translate : ')
        while (example != 'n'):
            example = input('write an example (or press n) : ')
            if (example != 'n'):
                examples.append(example)
        new_word = {
            word: {
                "translate": meaning,
                "examples": examples
            }
        }
        data.update(new_word)
        with open('words.json', 'w') as f:
            json.dump(data, f, indent=4)
        print('--- bye ---')
    else:
        print('--- bye ---')
