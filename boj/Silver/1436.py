from math import log10
n = int(input())

num = 666
pre = 0
for _ in range(n - 1):
    if pre % 10 == 5:
        if pos == 9:
            pre += 2
        pos += 1
    else:
        pos = -1
        pre += 1

print(pre, 666, pos)