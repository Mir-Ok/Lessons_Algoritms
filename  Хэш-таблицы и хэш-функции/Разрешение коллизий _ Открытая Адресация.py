""" Коллизии не победить, надо научиться с ними обходиться

Если текущий ключ занят, то пробуем положить в следующий за ним,
пока не найдем свободное. Пробирование - ищем свободное место, если идем
подряд - линейное пробирование """


""" Применение

Добавление и поиск элемента по времени не зависят от размера массива
Это серьезно улучшает производительность,так как нет полного обхода, 
как в списке
 
"""