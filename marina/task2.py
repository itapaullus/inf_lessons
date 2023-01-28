n = int(input())
a_join = [int(i) for i in input().split()]
a_diff = [int(i - a_join[0]) for i in a_join[1:]]
trg = set([i + 1 for i in range(n - 1)])
d1 = 0
for mod in range(2 * n - 1):
    lst = [a_diff[i] / a_diff[mod] for i in range(mod, 2 * n - 1)]
    print(lst)
    if trg.intersection(lst) == trg:
        d1 = a_diff[mod]
        break

print(*[a_join[0] + d1 * i for i in range(n)])
