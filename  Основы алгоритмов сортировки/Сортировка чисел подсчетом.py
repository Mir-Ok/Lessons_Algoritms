""" Самая быстрая

За одно сравнение мы получаем 1 бит информации, и поэтому нельзя сделать
сортировку быстрее, чем O(N) """

import math


def sorter(a, b):

    d = (a + b) / 2 + abs(a - b) / 2
    c = a+b-d
    return c, d


q = 10
w = 12
print(sorter(q, w))

