import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

d = [[] for _ in range(n)]

queue = [(0, 0)]

while queue:
    w, i = heappop(queue)

    if len(d[i]) != 0 and - d[i][0] < w:
        continue

    for node, weight in graph[i]:
        if len(d[node]) < k:
            heappush(d[node], - (w + weight))
            heappush(queue, ((w + weight), node))
        else:
            t = -heappop(d[node])
            heappush(d[node], -min(t, w + weight))
            heappush(queue, (min(t, w + weight), node))

print(d)

for val in d:
    try:
        print(-heappop(val))
    except:
        print(-1)
