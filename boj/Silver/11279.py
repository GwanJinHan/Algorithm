import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    x = int(input())
    if x == 0:
        try:
            print(-heappop(hq))
        except:
            print(0)

    else:
        heappush(hq, -x)
