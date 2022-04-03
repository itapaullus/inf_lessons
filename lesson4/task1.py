# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью
# данного алгоритма.

data = 'XXXXYXYZXXYXXYXZZXZXXXYXXYYZYXXXZXXYXX'


def calc_str(s: str):
    prev_char = ''
    result = 1
    max_result = 0
    for i in s:
        if i != prev_char:
            result += 1
        else:
            if result > max_result:
                max_result = result
            result = 1
        prev_char = i
    if result > max_result:
        max_result = result
    return max_result


print(calc_str(data))
