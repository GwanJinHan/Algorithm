import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
hq = []
ans = []
for _ in range(n):
    num = int(input())

    if num == 0:
        try:
            ans.append(heappop(hq)[1])
        except:
            ans.append(0)
    else:
        heappush(hq, (abs(num), num))

for val in ans:
    print(val)
