import heapq
import sys
input = sys.stdin.readline

t = int(input())

h = []

for _ in range(t):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(h))
        except:
            print(0)
    else:
        heapq.heappush(h, x)
