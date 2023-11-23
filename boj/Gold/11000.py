from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort()
hq = []
ans = 1
for a, b in arr:
    if len(hq) == 0:
        heappush(hq, b)
    else:
        if a < hq[0]:
            ans += 1
        else:
            heappop(hq)
        heappush(hq, b)

print(ans)