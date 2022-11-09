int_strings = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7,
               'восемь': 8, 'девять': 9,
               'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
               'пятнядцать': 15,
               'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20,
               'тридцать': 30,
               'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
               'девяносто': 90, }

numerator_strings = {'одна': 1, 'две': 2}

divider_strings = {
    'первых': 1, 'первая': 1, 'вторых': 2, 'вторая': 2, 'третьих': 3,
    'третья': 3, 'четвертых': 4, 'четвертая': 4, 'пятых': 5, 'пятая': 5, 'шестых': 6, 'шестая': 6, 'седьмых': 7,
    'седьмая': 7, 'восьмых': 8, 'восьмая': 8, 'девятых': 9, 'девятая': 9, 'десятых': 10, 'десятая': 10,
    'одиннадцатых': 11, 'одиннадцатая': 11, 'двенадцатых': 12, 'двенадцатая': 12, 'тринадцатых': 13, 'тринадцатая': 13,
    'четырнадцатых': 14,
    'четырнадцатая': 14, 'пятнадцатых': 15, 'пятнадцатая': 15, 'шестнадцатых': 16, 'шестнадцатая': 16,
    'семнадцатых': 17,
    'семнадцатая': 17, 'восемнадцатых': 18, 'восемнадцатая': 18, 'девятнадцатых': 19, 'девятнадцатая': 19,
    'двадцатых': 20, 'двадцатая': 20,
    'тридцатых': 30, 'тридцатая': 30, 'сороковых': 40, 'сороковая': 40, 'пятидесятых': 50, 'пятидесятая': 50,
    'шестидесятых': 60, 'шестидесятая': 60, 'семидесятых': 70, 'семидесятая': 70, 'восьмидесятых': 80,
    'восьмидесятая': 80,
    'девяностых': 90, 'девяностая': 90, }


def get_nod(a, b):
    if not a or not b:
        return 1
    n_max, n_min = max(a, b), min(a, b)
    if n_max == n_min:
        return n_max
    else:
        return get_nod(n_max - n_min, n_min)


def str_to_fractions(s: tuple):
    """
    get numerator and divider of fraction
    :param s: tuple of words, btw: ('двадцать','одна','пятьдесят','первая')
    :return: tuple with numerator and divider
    """
    numerator = []  # числитель
    divider = []  # знаменатель
    div_flag = False
    for i in range(len(s)):
        current_num = int_strings.get(s[i])
        if not current_num:  # если не нашли в целочисленных словах, посмотрим в окончаниях числителя
            current_num = numerator_strings.get(s[i])  # если нашли тут, значит это точно конец числителя
            if current_num:
                numerator.append(current_num)
                div_flag = True
                continue  # идем к следующему числу
        # проверим в знаменателях, возможно это случай типа двадцать тридцатых
        if not current_num:
            current_num = divider_strings.get(s[i])
            if current_num:
                divider.append(current_num)
                break  # сразу можно выходить, больше ничего не будет
        if not div_flag:
            numerator.append(current_num)
            if current_num > 19 and not current_num % 10:  # если это числа типа 20-30-40-50.. и мы не понимаем, что дальше
                # смотрим следующее слово в целых числах
                next_num = int_strings.get(s[i + 1])
                try:
                    if next_num < 10:  # это вторая часть числителя. Например, "двадцать ПЯТЬ"
                        continue  # раз не упали на условии, значит число нашлось, оно часть числителя и все норм, обработается в следующей итерации
                    else:  # это число уже относится к знаменателю
                        div_flag = True
                        continue
                except TypeError:
                    pass  # если тут упали, значит next_num is None, и в целых числах слова нет
                div_flag = True
                continue
            elif current_num < 10:
                div_flag = True
        else:
            divider.append(current_num)
    # проверим корректность и упростим дроби
    num, div = sum(numerator), sum(divider)
    if num >= div:
        print('Числитель дроби должен быть меньше знаменателя')
    else:  # попробуем упростить
        nod = get_nod(num, div)
        return num / nod, div / nod


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
    return ''


def str_to_num(s: tuple):
    """
    Format string text to tuple with integer and fraction part: (2, (3,5))
    :param s:
    :return: int
    """
    result = 0
    fraction = (0, 1)
    # ("один", "и", "четыре", "пятых")
    if 'и' in s:  # дробь
        fraction = str_to_fractions(s[s.index('и') + 1:])
        s = s[:s.index('и')]
    elif set(divider_strings.keys()).intersection(set(s)):  # если есть слова, которые содержатся в знаменателях
        fraction = str_to_fractions(s)
        return 0, fraction
    try:
        for i in s:
            result += int_strings.get(i)
        if result < 0 or result >= 100:
            print('Некорректное число')
            return None
        return result, fraction
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
        left, right = str_to_num(tuple(word_list[:sign_pos])), str_to_num(tuple(word_list[sign_pos + 1:]))
        if left and right and sign:
            return (left, right, sign)
        return None
    else:
        print('Некорректный ввод')


def calc_result(data: tuple):
    """
    return tuple with integer part of result, numerator and divider
    :param data:
    :return:
    """
    if data:
        # return int_to_str(eval(f'{data[0]}{data[2]}{data[1]}'))
        # (2, (3, 5)), (1, (0,1)), '+'
        if data[2] == '+':
            numerator = data[0][1][0] * data[1][1][1] + data[0][1][1] * data[1][1][0]
            divider = data[0][1][1] * data[1][1][1]
            int_part = data[0][0] + data[1][0]
            int_part += numerator // divider
            numerator = numerator % divider
        elif data[2] == '-':
            int_part = data[0][0] - data[1][0]
            numerator = data[0][1][0] * data[1][1][1] - data[0][1][1] * data[1][1][0]
            divider = data[0][1][1] * data[1][1][1]
            if numerator < 0:
                numerator += divider
                int_part -= 1
        elif data[2] == '*':
            print('Реализовать самостоятельно!') # todo умножение
        else:
            print('Некорректный ввод')
            return None
        nod = get_nod(numerator, divider)
        return int_part, numerator / nod, divider / nod
    else:
        print('Выражение невозможно вычислить')


def result_to_str(i: tuple):
    res = ''
    if i[0] > 99 or i[0] < 0 or i[1] > 99 or i[1] < 0 or i[2] > 99 or i[2] < 0:
        return f'Вывод строкой не поддерживается: результат {i[0]} {i[1]}/{i[2]}'
    if i[0] < 10 or not i[0] % 10:
        res += get_value(int_strings, i[0])
    else:
        res += get_value(int_strings, i[0] - i[0] % 10) + ' ' + get_value(int_strings, i[0] % 10)
    if i[1]:  # если есть дробная часть
        if i[1] < 10 or not i[0] % 10:
            # подходящее слово будет либо в целых, либо в числителях
            num_str = get_value(int_strings, i[1])
            if not num_str:
                num_str = get_value(numerator_strings, i[1])
            res += ' и '+num_str
        else:
            res += ' и '+get_value(int_strings, i[1] - i[1] % 10) + ' ' + get_value(int_strings, i[1] % 10) + ' ' + get_value(numerator_strings, i[1] % 10)
        if i[1] < 21 or not i[0] % 10:
            # подходящее слово будет в знаменателях
            div_str = get_value(divider_strings, i[2])
            res += ' '+div_str
        else:
            res += ' ' + get_value(int_strings, i[2]-i[2]%10) + get_value(divider_strings, i[2] % 10)
    return res


print(result_to_str(calc_result(parse_string('два и три десятых плюс три десятых'))))
print(result_to_str(calc_result(parse_string('два и одна двадцатая плюс восемь двадцатых'))))

# print(calc_result(parse_string('двадцать плюс тридцать')))

# print(str_to_num(("одна", "десятая")))
