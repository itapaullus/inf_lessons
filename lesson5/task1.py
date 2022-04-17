# Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.

# вариант 1, через функцию
def abs_value(x):
    return abs(x)


def list_sort(lst: list):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst


a = [1, -4, 2, -3, 56]
print(list_sort(a))




