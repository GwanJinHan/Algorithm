import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

start, end = map(lambda x: int(x) - 1, input().split())

d = [sys.maxsize] * n
d[start] = 0
r = [[start + 1] for i in range(n)]

queue = [(0, start)]

while queue:
    w, i = heappop(queue)

    if d[i] < w:
        continue

    for node, weight in graph[i]:
        if d[i] + weight < d[node]:
            d[node] = d[i] + weight
            heappush(queue, (d[node], node))
            r[node] = r[i] + [node + 1]
        elif d[i] + weight == d[node]:
            r[node] = r[i] + [node + 1]
print(d[end])
print(len(r[end]))
print(*r[end])
