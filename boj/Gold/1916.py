import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

start, end = map(int, input().split())

d = [sys.maxsize] * n
d[start - 1] = 0

queue = [(0, start - 1)]

while queue:
    w, i = heappop(queue)

    if w > d[i]:
        continue

    for node, weight in graph[i]:
        if d[i] + weight < d[node]:
            d[node] = d[i] + weight
            heappush(queue, (d[node], node))

print(d[end - 1])
