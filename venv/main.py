from tabulate import tabulate

word = input('Введите сообщение:\n').upper()
_list = [int(x) for x in input('Введите шифр:\n').split(',')]
_dict = {key:'' for key in _list}

count = 0
while count < len(word):
    for key in _dict:
        if count < len(word):
            _dict[key] += word[count]
            count+=1
        else:
            _dict[key] += '-'


print(tabulate(_dict, headers='keys', tablefmt='grid'))

sort = sorted(_dict)
text = ''
for key in sort:
    text += _dict[key]

print(text)