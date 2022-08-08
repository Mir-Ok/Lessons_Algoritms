# Задача - найти все неповторяющиеся номера в списке

# Метод грубой силы, brut force

""" Большое время, повторится столько раз, сколько элементов N раз
внутри условие каждый раз столько раз, сколько в новом списке (1+2+3 ... + N) = N/2
Общее время N * N/2 = N**2 / 2 - квадратичная зависимость """

numbers_list = [+79046190750, +79046190750, +79043307650, +79111567399]
list_unique = []

for number in numbers_list:
    if number not in list_unique:
        list_unique.append(number)
print(list_unique)









