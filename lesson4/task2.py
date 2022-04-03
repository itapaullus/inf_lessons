# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов Y.

data = 'XZXZXZXZXZXXXZXZXZY'


def calc_str(s: str):
    result = 0
    max_result = 0
    for i in s:
        if i == 'Y':
            result += 1
        else:
            if result > max_result:
                max_result = result
            result = 0
    if result > max_result:
        max_result = result
    return max_result


print(calc_str(data))
