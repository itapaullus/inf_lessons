# вариант 3 через map (не совсем корректный)
def list_sort(lst: list):
    b = list(map(abs, lst))
    b.sort(reverse=True)
    return b


a = [1, -4, 2, -3, 56]
print(list_sort(a))
