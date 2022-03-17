# def summ_2_number(a, b):
#     i = 10
#     result = (a + b) * i
#     return result
#
#
# def print_result(a):
#     print(f'Результат работы функции равен {a}')
#
#
# x = summ_2_number(3, 5) + summ_2_number(4, 8) + summ_2_number(2, 2)     # глобальная переменная
# print_result(x)
# print_result(123465)


# def get_nod(a, b):
    # cnt = 0
    # lst_a = []
    # for i in range(1, a+1):
    #     cnt += 1
    #     if a % i == 0:
    #         lst_a.append(i)
    # for i in range(1, b + 1):
    #     cnt += 1
    #     if b % i == 0:
    #         if i in lst_a:
    #             max_res = i
    # print(f'Количество делений: {cnt}')
    # return max_res


cnt = 0


def get_nod(a, b):
    global cnt
    if a == 0 or b == 0:
        cnt += 1
        return max(a, b)
    else:
        cnt += 1
        if a > b:
            return get_nod(a-b, b)
        else:
            return get_nod(a, b-a)


def get_nod2(a, b):
    global cnt
    while a > 0 and b > 0:
        cnt += 1
        if a > b:
            a = a-b
        else:
            b = b-a
    print(max(a, b))


def get_simple_divs(a):
    pass

# print(get_nod2(2, 2312))
print(cnt)

# 1
# 2-2-3 = 12
