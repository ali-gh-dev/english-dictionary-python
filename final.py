from difflib import get_close_matches
import json

# adds color to the output
data = json.load(open('words.json', encoding='utf-8'))


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


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


def start():
    global data
    print('\n')
    print(color.BOLD + color.PURPLE + '=========== Hi ===========' + color.END)
    print('\n')

    word = input('search a word : ')
    alternate = get_close_matches(word, data.keys())

    if word in data:
        translate(word)
    elif len(alternate) > 0:
        check = input(color.PURPLE + "Did you mean %s ? y/n : " %
                      alternate[0] + color.END)
        if check in ['Y', 'y']:
            translate(alternate[0])
        elif check in ['N', 'n']:
            print('--- bye ---')
        else:
            print('--- wrong input ---')
    else:
        print('--- not found ---')
        check = input(
            color.PURPLE + 'Should I add this word to dictionary?  y/n : ' + color.END)
        examples = []
        example = ''
        if check in ['Y', 'y']:
            meaning = input('Meaning : ')
            while (example != 'n'):
                example = input(
                    color.PURPLE + 'write an example (or press n) : ' + color.END)
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


if __name__ == '__main__':
    start()
