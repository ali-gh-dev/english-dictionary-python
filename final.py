from difflib import get_close_matches
import json

def translate(word):
    global data
    if word in data:
        print('-' *  20)
        print('Translate : ')
        print(data[word]['translate'])
        print('-' *  20)
        print('Examples : ')
        for ex in data[word]['examples']:
            print(ex)
        print('-' *  20)


data = json.load(open('words.json', encoding='utf-8'))

print('\n')
print('=========== Hi ===========')
print('\n')
word  = input('search a word : ')
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
    # todo : complete this part
    print('--- oops not found ---')
