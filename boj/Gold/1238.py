import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a - 1].append((b - 1, t))

arr = [0] * n

for start in range(n):  # 각각의 학생에 대하여
    d = [sys.maxsize] * n
    d[start] = 0

    queue = [(0, start)]

    while queue:
        w, index = heappop(queue)

        if w > d[index]:
            continue

        for node, weight in graph[index]:
            if d[index] + weight < d[node]:
                d[node] = d[index] + weight
                heappush(queue, (d[node], node))

    arr[start] += d[x - 1]

    if start == x - 1:
        for i in range(n):
            arr[i] += d[i]

print(max(arr))
