""" В односвязном есть проблема с удалением последнего элемента, так
как ссылка есть только на следующий элемент и на начало. И с удалением с конца
надо было снова искать последний, сложность О(N)

В двухсвязном мы храним ссылку на следующий и предыдущий, а так же на его
начало и конец
Добавление - сначала создаем элемент, потом вешаем ссылку на него
Если в середину - сначала создаем, потом перевешиваем ссылки
Удаление - вынимаем элемент и соединяем ссылки от крайних между собой """