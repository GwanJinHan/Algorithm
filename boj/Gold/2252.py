from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnts = [0] * n
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    cnts[b - 1] += 1

queue = deque()

for i, c in enumerate(cnts):
    if c == 0:
        queue.append(i)
ans = []
while queue:
    v = queue.popleft()
    ans.append(v + 1)

    for i in graph[v]:
        cnts[i] -= 1
        if cnts[i] == 0:
            queue.append(i)

print(*ans)
