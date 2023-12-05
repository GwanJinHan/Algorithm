from collections import defaultdict as dd
n = input()
d = dd(int)
for t in n:
    if t == '6' or t == '9':
        d[69] += 1
    else:
        d[int(t)] += 1

d[69] = (d[69] + 1) // 2

print(max(d.values()))
