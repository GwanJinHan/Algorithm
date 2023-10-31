import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input()) - 1

graph = [[] for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

d = [sys.maxsize] * v
d[start] = 0

queue = [(0, start)]

while queue:
    w, i = heappop(queue)

    if w > d[i]:
        continue

    for node, weight in graph[i]:
        if d[i] + weight < d[node]:
            d[node] = d[i] + weight
            heappush(queue, (d[node], node))

for ans in d:
    print(ans if ans != sys.maxsize else "INF")
