# Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.
from lesson3 import task2
def date(d,m,g):
    m30 = [4, 6, 9, 11]
    m31 = [1, 3, 5, 7, 8, 10, 12]
    if m in m30 and 0<d<=30:
        return True
    elif m in m31 and 0<d<=31:
        return True
    elif m == 2:
        v = task2.visok(g)
        if v == 'Високосный' and 0<d<30:
            return True
        elif v == 'Обычный' and 0<d<29:
            return True
        else:
            return False
    else:
        return False
print(date(29,2,2021)   )

