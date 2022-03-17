def task2():
    a = ''
    for i in reversed(range(11)):
        a = a + str(i) + ', '
    print(a + 'поехали!')


def task3():
    for mc in range(6):
        if mc == 0:
            print('У вас нет сообщений')
        else:
            print(f'Новых сообщений: {mc}')



def task4():
    for i in range(24):
        if i <6:
            print('Доброй ночи!')
        elif i<12:
            print('Доброе утро!')
        elif i<18:
            print('Добрый день!')
        elif i<23:
            print('Добрый вечер!')
        else:
            print('Доброй ночи!')



def task5():
    for mc in range(21):
        if mc == 0:
            print('У вас нет новых сообщений')
        elif mc == 1:
            print('У вас 1 новое сообщение')
        elif mc <= 4:
            print(f'У вас {mc} новых сообщения')
        else:
            print(f'У вас {mc} новых сообщений')


may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]

# Допишите эту функцию
def comfort_count(temperatures):
    count = 0
    for temp in temperatures:
        if 22 <= temp <= 26:
            count += 1
    return count


def calc_cube_perimeter(l):
    sdr = 12*l
    return sdr






if __name__ == '__main__':
    a = calc_cube_perimeter(3)
    print(a*8)

