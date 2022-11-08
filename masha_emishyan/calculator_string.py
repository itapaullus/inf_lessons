words_to_numbers = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7,
                    'восемь': 8, 'девять': 9,
                    'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
                    'пятнядцать': 15,
                    'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20,
                    'тридцать': 30,
                    'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90}
# todo дроби


def get_value(d: dict, value: int):
    """
    return first key of dict by value
    :param d: dict to finding
    :param value: find predicate
    :return: str
    """
    for rec in d.items():
        if rec[1] == value:
            return rec[0]
    return None


def str_to_int(s: tuple):
    """
    Format string text to int
    :param s:
    :return: int
    """
    try:
        result = 0
        for i in s:
            result += words_to_numbers.get(i)
        if result < 0 or result >= 100:
            print('Некорректное число')
            return None
        return result
    except TypeError:
        return None


def parse_string(s: str):
    """
    Find left and right parts of operation
        btw return (123, 345, '+')
    :param s:
    :return: tuple
    """
    result = tuple()
    word_list = s.split()
    sign_pos = None
    for i in (('плюс', '+'), ('минус', '-'), ('умножить', '*')):
        try:
            sign_pos = word_list.index(i[0])
            sign = i[1]
            break
        except ValueError:
            pass
    if sign_pos:
        left, right = str_to_int(tuple(word_list[:sign_pos])), str_to_int(tuple(word_list[sign_pos + 1:]))
        if left and right and sign:
            return (left, right, sign)
        return None
    else:
        print('Некорректный ввод')


def calc_result(data: tuple):
    if data:
        return int_to_str(eval(f'{data[0]}{data[2]}{data[1]}'))
    else:
        print('Выражение невозможно вычислить')


def int_to_str(i: int):
    # 53
    if i > 99 or i < 1:
        print(f'Вывод строкой не поддерживается: результат {i}')
    if i < 10 or not i % 10:
        return get_value(words_to_numbers, i)
    else:
        return get_value(words_to_numbers, i - i % 10) + ' ' + get_value(words_to_numbers, i % 10)


print(calc_result(parse_string('двадцать плюс тридцать')))
