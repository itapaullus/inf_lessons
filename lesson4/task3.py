# Работа со строками



data = 'XZXZXZXZXZXXXZXZXZY'
arr = [1, 2, 3, 43, 54, 5]

for i in range(len(arr)):
    print(f'Элемент под номером {i} равен {arr[i]}')


def str_cycle(s: str):
    # for i in range(len(s)):
    #     print(s[i])
    for i in s:
        print(i)


# str_cycle(data)
