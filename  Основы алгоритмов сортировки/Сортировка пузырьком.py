""" Сортировка пузырьком Bubble

В процессе сортировки пузырьком происходит попарное сравнение соседних
элементов массива, начиная с нулевого. После первой итерации самое большое
число окажется на месте последнего, причем в дальнейших итерациях это значение
уже задействоваться не будет (по сути, мы получим n-1 сравнений).
Далее алгоритм находит второй по величине элемент, который ставится
на предпоследнее место, потом третий и пр.
В результате на месте нулевого элемента (не забываем, что нумерация в массиве
начинается с нуля) окажется наименьшее число, а на месте последнего
элемента – наибольшее. То есть мы можем сказать, что элементы от большего
к меньшему «всплывают» по аналогии с пузырьками.

Проговорим алгоритм еще раз:

1. Текущий элемент сравнивается с последующим.
2. Если последующий меньше или больше, они меняются местами.
3. Когда сортировка заканчивается, алгоритм прекращает работу,
   иначе снова происходит переход на шаг № 1.

Важно понимать, что при реализации сортировки применяют 2 цикла:
основной и вложенный (внутренний цикл).
По результатам одного прохода внутреннего цикла самый большой элемент
смещается в конец массива, тогда как самый маленький перемещается к началу
(на одну позицию).

Далее последний уже не трогаем, потом предпоследний.

Асимптотика - О(N**2), потому что в худшему случае мы переберем N элементов
1+2+3...+N раз, что равно N*N/2 """

from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

