from heapq import heappop, heappush
import sys
input = sys.stdin.readline

t = int(input())
INF = sys.maxsize
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(d):
        a, b, time = map(int, input().split())
        graph[b - 1].append((a - 1, time))

    q = [(0, c - 1)]
    d = [INF] * n
    d[c - 1] = 0

    while q:
        w, i = heappop(q)

        if d[i] < w:
            continue

        for node, weight in graph[i]:
            if weight + d[i] < d[node]:
                d[node] = weight + d[i]
                heappush(q, (d[node], node))
    cnt = 0
    ans = -1
    for v in d:
        if v != INF:
            cnt += 1
            if ans < v:
                ans = v

    print(cnt, ans)
