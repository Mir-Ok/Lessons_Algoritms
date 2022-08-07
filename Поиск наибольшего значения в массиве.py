# Поиск наибольшего значения
import time

digits = [i for i in range(10000000)]

# сортировка через встроенную функцию
tic1 = time.perf_counter()
max_digit_sort = max(digits)
toc1 = time.perf_counter()
print(f"Вычисление заняло {toc1 - tic1:0.5f} секунд")
print(max_digit_sort)  # --> Вычисление заняло 0.13542 секунд


# сортировка через цикл
tic2 = time.perf_counter()
maximum = 0
for digit in digits:
    if digit > maximum:
        maximum = digit
toc2 = time.perf_counter()
print(f"Вычисление заняло {toc2 - tic2:0.5f} секунд")
print(maximum)  # --> Вычисление заняло 1.07688 секунд


# сортировка через цикл с max
tic3 = time.perf_counter()
maximum = 0
for k in range(len(digits)):
    maximum = max(maximum, digits[k])
toc3 = time.perf_counter()
print(f"Вычисление заняло {toc3 - tic3:0.5f} секунд")
print(maximum)  # --> Вычисление заняло 2.91844 секунд

