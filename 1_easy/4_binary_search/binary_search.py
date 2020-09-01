"""
4. Алгоритм бинарного поиска

Идея проекта. Алгоритм бинарного поиска — очень эффективный способ
поиска элемента в длинном списке.
Идея состоит в том, чтобы реализовать алгоритм, который ищет элемент
в списке методом деления
списка пополам и сравнения значения середины с искомым значением.

"""


def time_of_function(function):
    """Замер времени выполнения функции"""

    def wrapped(*args, **kwargs):
        import decimal
        import time

        start_time = time.time()
        res = function(*args, **kwargs)
        end_time = time.time()
        result = decimal.Decimal(end_time) - decimal.Decimal(start_time)
        print(result)

        return res

    return wrapped


@time_of_function
def binary_search(sorted_int_list, element):
    print('Поиск с помощью бинарного алгоритма')
    low = 0
    high = len(sorted_int_list) - 1

    while low <= high:
        mid = int((low + high) / 2)  # Определяем середину списка

        guess = sorted_int_list[mid]  # берем значение индекса половины списка
        if guess == element:  # если это значение равно искомому элементу
            return mid  # возвращаем его
        if guess > element:  # если значение индекса больше искомого элемента
            high = mid - 1  # задаем верхнюю границу равной вычисленной раньше половине списка - 1
        else:
            low = mid + 1  # если меньше, то задаем нижнюю границу равной вычисленной раньше половине списка + 1
    return 'Item not found.'


# декарируем для замеров времени
@time_of_function
def ind(l: list, i: int):
    print('поиск встроенным методом list.index')
    res = l.index(i)
    return res


my_list = [x for x in range(1, 10087600)]
print('Список создан')
item = my_list[-2]
print('Искомое значение', item)

a = binary_search(my_list, item)
b = ind(my_list, item)
print(a)
