import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
l = []
r = []
a, b = int(input()), int(input())
if a < b:
    l.append(-a)
    r.append(b)
    print(a)
    print(a)
else:
    l.append(-b)
    r.append(a)
    print(b)
    print(b)

ans = []
for i in range(1, n + 1):

    num = int(input())
    if i == 1 or i == 2:
        heappush(r, num)

    if r[0] >= num:
        heappush(l, -num)
    else:
        heappush(r, num)

    if i % 2 == 0:
        ans.append(r[0] if r[0] < -l[0] else -l[0])
    else:
        ans.append(r[0] if len(r) > len(l) else -l[0])

for val in ans:
    print(val)
