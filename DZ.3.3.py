list_r = [1, 2, 3, 4, 5]
print('Для выхода - введите "000"')
print(f"Рейтинг - {list_r}")
num = int(input("Введите число: "))
while num != 000:
    for el in range(len(list_r)):
        if list_r[el] == num:
            list_r.insert(el + 1, num)
            break
        elif list_r[0] < num:
            list_r.insert(0, num)
        elif list_r[-1] > num:
            list_r.append(num)
        elif list_r[el] > num and list_r[el + 1] < num:
            list_r.insert(el + 1, num)
    print(f"Текущий список - {list_r}")
    num = int(input("Введите число: "))
