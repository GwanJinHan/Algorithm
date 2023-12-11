from collections import deque
import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    hq = [(0, s)]
    dist = [INF] * n
    path = [[] for _ in range(n)]

    while hq:
        w, i = heappop(hq)

        if dist[i] < w:
            continue

        for node, weight in graph[i]:
            if dist[node] > weight + w:
                dist[node] = weight + w
                heappush(hq, (dist[node], node))
                path[node] = [i]
            elif dist[node] == weight + w:
                path[node].append(i)

    x = d
    q = deque([x])
    shortest_edges = set()
    visit = set()
    while q:
        cur = q.popleft()
        if cur in visit:
            continue
        visit.add(cur)
        for v in path[cur]:
            shortest_edges.add((v, cur))
            if cur != s:
                q.append(v)

    hq = [(0, s)]
    dist = [INF] * n
    new_graph = [[] for _ in range(n)]
    for i in range(n):
        for node, weight in graph[i]:
            if (i, node) not in shortest_edges:
                new_graph[i].append((node, weight))
    while hq:
        w, i = heappop(hq)

        if dist[i] < w:
            continue

        for node, weight in new_graph[i]:
            if dist[node] > weight + w:
                dist[node] = weight + w
                heappush(hq, (dist[node], node))

    print(dist[d] if dist[d] != INF else -1)
