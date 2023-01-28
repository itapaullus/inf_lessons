'''
№ 5
Сумма подряд идущих
Формулировка этой задачи очень проста: сколько существует различных непрерывных последовательностей подряд идущих натуральных чисел, которые в сумме дают заданное число n?

Входные данные
На вход подается n, не превосходящее 1012.

Выходные данные
Выведите одно натуральное число — ответ на задачу.

Система оценки
Баллы за каждый тест начисляются независимо.

Пояснение к примеру
В примере нужно найти количество непрерывных подпоследовательностей подряд идущих натуральных чисел, дающих в сумме число 15. Таких подпоследовательностей 4:

1. 1+2+3+4+5=15
2. 4+5+6=15
3. 7+8=15
4. 15=15

Ввод
15

Вывод
4
'''
# Задача 5
x = int(input())
res = 0
for next in range(1, x + 1):
    d = 0
    new_sum = 0
    while new_sum < x:
        new_sum += next + d
        d += 1
        if new_sum == x:
            res += 1

print(res)
