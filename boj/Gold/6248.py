import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, x = map(int, input().split())
INF = sys.maxsize
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

q = [(0, x - 1)]
d = [INF] * n
d[x - 1] = 0

while q:
    w, i = heappop(q)

    for node, weight in graph[i]:
        if weight + d[i] < d[node]:
            d[node] = weight + d[i]
            heappush(q, (d[node], node))

print(max(d) * 2)
