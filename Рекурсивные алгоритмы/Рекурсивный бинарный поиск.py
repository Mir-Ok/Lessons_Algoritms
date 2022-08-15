""" Рекурсия - функция вызывает сама себя до крайнего случая """

a = [1, 2, 3, 3, 4]


# итеративно
def binary_search(key):
    start = -1
    end = len(a)
    while start + 1 < end:
        m = int((start + end) / 2)
        if a[m] >= key:
            end = m
        else:
            start = m

    return end


print(binary_search(3))


""" Чтобы реализовать алгоритм рекурсивного бинарного поиска, 
мы должны сначала найти цель в отсортированном порядке, 
среднее значение проверяется, чтобы определить, является ли оно целью. 
Если среднее значение не является целевым, последовательность разбивается 
пополам, затем проверяется первая или вторая половина, 
чтобы найти целевое значение, просматривая средний элемент. 

Вот свойства, которым должны удовлетворять все рекурсивные решения:

    Рекурсивное решение должно иметь базовый случай.
    Рекурсивное решение должно иметь рекурсивный случай.
    Рекурсивное решение должно продвигаться к базовому случаю.
    
"""


# рекурсивно
def rec_binary_search(target, sequence, first, last):
    if first > last:
        return False
    else:
        mid = (last + first) // 2
        if sequence[mid] == target:
            return True
        elif target < sequence[mid]:
            return rec_binary_search(target, sequence, first, mid-1)
        else:
            return rec_binary_search(target, sequence, mid + 1, last)


