import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

v1, v2 = map(int, input().split())

# 1번 -> v1 -> v2 -> n번
# 1번 -> v2 -> v1 -> n번
# v1, v2에서 모든 정점으로의 최단거리만 구하면 됨.

d_one = [sys.maxsize] * n
d_one[v1 - 1] = 0
d_two = [sys.maxsize] * n
d_two[v2 - 1] = 0

queue = [(0, v1 - 1)]

while queue:
    w, i = heappop(queue)

    if d_one[i] < w:
        continue

    for node, weight in graph[i]:
        if d_one[i] + weight < d_one[node]:
            d_one[node] = d_one[i] + weight
            heappush(queue, (d_one[node], node))

queue = [(0, v2 - 1)]

while queue:
    w, i = heappop(queue)

    if d_two[i] < w:
        continue

    for node, weight in graph[i]:
        if d_two[i] + weight < d_two[node]:
            d_two[node] = d_two[i] + weight
            heappush(queue, (d_two[node], node))

dis = min(d_one[0] + d_one[v2 - 1] + d_two[n - 1],
          d_two[0] + d_two[v1 - 1] + d_one[n - 1])

print(dis if dis < sys.maxsize else -1)
