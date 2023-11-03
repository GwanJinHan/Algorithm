import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, r = map(int, input().split())
ans = 0
graph = [[] for _ in range(n)]

item_cnt = list(map(int, input().split()))

for _ in range(r):
    a, b, i = map(int, input().split())
    graph[a - 1].append((b - 1, i))
    graph[b - 1].append((a - 1, i))

for start in range(n):
    queue = [(0, start)]
    d = [sys.maxsize] * n
    d[start] = 0

    while queue:
        w, i = heappop(queue)

        if d[i] < w:
            continue

        for node, weight in graph[i]:
            if d[i] + weight < d[node]:
                d[node] = d[i] + weight
                heappush(queue, (d[node], node))

    cnt = 0
    for i in range(n):
        if d[i] <= m:
            cnt += item_cnt[i]

    ans = max(ans, cnt)

print(ans)
