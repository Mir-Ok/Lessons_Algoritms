""" При помощи бинарного поиска ищем индекс, куда вставить

Есть вариант просто добавить в конец и отсортировать, но это занимает
N**2/2 операций, а бинарный поиск имеет логарифмическую зависимость,
и она растет не так быстро, как квадратичная

Питон имеет для этого встроенные функции """

# используем списки
# append - один в конец

my_input = ['Engineering', 'Medical']
my_input.append('Science')  # --> ['Engineering', 'Medical', 'Science']

# extend - список в конец
my_input = ['Engineering', 'Medical']
input1 = [40, 30, 20, 10]
my_input.extend(input1)  # --> ['Engineering', 'Medical', 40, 30, 20, 10]

# insert - вставка на указанное место
my_input = [1, 2, 3, 4, 5]
number = 25
index = 3
my_input.insert(index, number)  # --> [1, 2, 3, 25, 4, 5]


# модуль Array
import array

s1 = array.array('i', [1, 2, 3])  # --> array('i', [1, 2, 3])
s2 = array.array('i', [4, 5, 6])  # --> array('i', [4, 5, 6])

s3 = s1 + s2      # --> array('i', [1, 2, 3, 4, 5, 6])
s1.append(4)      # --> array('i', [1, 2, 3, 4])
s1.insert(0, 10)  # --> array('i', [10, 1, 2, 3, 4])
s1.extend(s2)     # --> array('i', [10, 1, 2, 3, 4, 4, 5, 6])


# NumPy Array
import numpy

arr1_insert = numpy.array([1, 23, 33])
arr2_insert = numpy.insert(arr1_insert, 1, 91)  # --> [ 1 91 23 33]

arr1_append = numpy.array([4, 2, 1])
arr2_append = numpy.append(arr1_append, [12, 13, 14])  # --> [ 4  2  1 12 13 14]
