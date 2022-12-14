""" Алгоритм заключается в принятии локально-оптимальных решений
на каждом этапе, допуская, что конечное решение так же окажется оптимальным

Например, задание с монетками за решения.
Есть N задач, у которых своя стоимость за решение и каждая занимает час
Есть К часов и надо выбрать задачи.

Мы сортируем задачи по стоимости, делаем реверс и берем К первых элементов,
решая сначала самую ценную задачу, потом самую ценную из оставшихся и пр.

Жадность - потому что в текущий момент берем самый жирный барыш и что будет
дальше не думаем.

Это не всегда хорошо, потому что выполнить за 4 часа можно 2 задачи
по 3 монеты каждая, либо хапнуть сразу на 3 часа и 5 монте, но потерять рабочий
час последний и тем самым получить всего 5 монет вместо 6

Можно попробовать считать удельную стоимость часа, но это тоже не
универсально. Аналогичные задачи мы решали при помощи генетики в УИИ

ТО есть мы можем жадностью решить только просты задачи, где время всех задач
одинаковое, а стоимость различная
"""