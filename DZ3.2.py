list_1 = input('Введите слова через пробел: ').split()
for q, el in enumerate(list_1, 1):
    print(q, el[0:10])