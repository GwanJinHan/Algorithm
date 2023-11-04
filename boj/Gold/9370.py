import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())  # 교차로, 도로, 목적지 후보 개수
    s, g, h = map(int, input().split())  # 출발지, 냄새맡은 곳

    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a - 1].append((b - 1, d))
        graph[b - 1].append((a - 1, d))

    arr = [int(input()) for _ in range(t)]  # 후보들

    # s -> g -> h -> 후보 : g - s , h - 후보 만 확인하면 됨 => 존재한다 : X < sysmaxsize
    # s -> h -> g -> 후보 : h - s , g - 후보 만 확인하면 됨
    # s ,g, h 만 구하면 됨

    d = [sys.maxsize] * n
    d[s - 1] = 0

    queue = [(0, s - 1)]

    while queue:
        w, i = heappop(queue)

        if d[i] < w:
            continue

        for node, weight in graph[i]:
            if d[i] + weight < d[node]:
                d[node] = d[i] + weight
                heappush(queue, (d[node], node))

    d_g = [sys.maxsize] * n
    d_g[g - 1] = 0

    queue = [(0, g - 1)]

    while queue:
        w, i = heappop(queue)

        if d_g[i] < w:
            continue

        for node, weight in graph[i]:
            if d_g[i] + weight < d_g[node]:
                d_g[node] = d_g[i] + weight
                heappush(queue, (d_g[node], node))

    d_h = [sys.maxsize] * n
    d_h[h - 1] = 0

    queue = [(0, h - 1)]

    while queue:
        w, i = heappop(queue)

        if d_h[i] < w:
            continue

        for node, weight in graph[i]:
            if d_h[i] + weight < d_h[node]:
                d_h[node] = d_h[i] + weight
                heappush(queue, (d_h[node], node))

    arr.sort()
    ans = []
    for val in arr:
        if d[val - 1] == d_g[s - 1] + d_h[val - 1] + d_g[h - 1]:
            ans.append(val)
        elif d[val - 1] == d_h[s - 1] + d_g[val - 1] + d_g[h - 1]:
            ans.append(val)
    print(*ans)
