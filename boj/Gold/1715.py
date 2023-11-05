from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    heappush(arr, int(input()))

ans = 0
while len(arr) > 1:
    x = heappop(arr)
    y = heappop(arr)
    ans += x + y
    heappush(arr, x + y)


print(ans)
