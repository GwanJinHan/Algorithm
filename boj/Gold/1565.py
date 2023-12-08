from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
times = [0] * n
cnts = [0] * n


for s in range(n):
    t, *ind = map(int, input().split())
    ind.pop()
    times[s] = t
    for d in ind:
        graph[d - 1].append(s)
        cnts[s] += 1

queue = deque()

for s in range(n):
    if cnts[s] == 0:
        queue.append(s)

dp = times.copy()

while queue:
    cur = queue.popleft()

    for i in graph[cur]:
        cnts[i] -= 1
        dp[i] = max(dp[i], times[i] + dp[cur])
        if cnts[i] == 0:
            queue.append(i)

for ans in dp:
    print(ans)
