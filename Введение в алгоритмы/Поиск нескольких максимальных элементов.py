# Поиск наибольшего значения
import time

# digits = [i for i in range(10000000)]
digits = [1, 2, 3, 147, 7, 9, 21, 52, 74, 89, 94, 121, 125, 145]
# сортировка через цикл с max
tic = time.perf_counter()

maximum = 0
for k in range(len(digits)):
    maximum = max(maximum, digits[k])

# удалим из перебора первый максимум
maximum2 = 0
for k in range(len(digits)):
    if digits[k] != maximum:
        maximum2 = max(maximum2, digits[k])

toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic:0.5f} секунд")
print(maximum)
print(maximum2)


