from difflib import get_close_matches
import json



data = json.load(open('words.json', encoding='utf-8'))

print('\n')
print('=========== Hi ===========')
print('\n')
word  = input('search a word : ')
if word in data:
    print('-' *  20)
    print('Translate : ')
    print(data[word]['translate'])
    print('-' *  20)
    print('Examples : ')
    for ex in data[word]['examples']:
        print(ex)
    print('-' *  20)
else:
    # todo : complete this part
    print('--- oops not found ---')
