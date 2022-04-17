a = 0
b = 0
x = int(input())
while x > 0:
    c = x % 2
    if c == 0:
        a += 1
    else:
        b += 1
    x = x//10

print(a)
print(b)
