# Функция по определению, является ли число простым


def is_simple(n: int):
    if n < 0:
        # raise ('Некорректный ввод');
        print('Некорректный ввод')
        return None
    if n < 3:
        return True
    for i in range(2, int(n**(1/2))+2):          # range [...)
        if n % i == 0:
            return False
    return True


print(is_simple(-2))
