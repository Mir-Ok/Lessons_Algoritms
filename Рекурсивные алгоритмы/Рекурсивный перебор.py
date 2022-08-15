""" Попробуем сгенерить пароль их 4 букв во всех комбинациях
Но много повторов, и при добавлении длины пароля - придется вложить еще циклы

Рекурсивный перебор поможет? он сам вложит необходимое """

import string

# итеративно
# letters = string.ascii_lowercase
# for i in letters:
#     for j in letters:
#         for k in letters:
#             for m in letters:
#                 s = i + j + k + m
#                 print(s)


# рекурсивно
def rec(word, h):
    letters1 = string.ascii_lowercase
    if len(word) == h:
        print(word)
        return
    for c in letters1:
        if word != c:  # доработать условие ниже
            rec(word + c, h)


rec('', 3)

""" Добавим в условие, что мы не выводим на печать те пароли, где буквы 
повторяются """
