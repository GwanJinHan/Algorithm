from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    cnts = [0] * n
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        cnts[b - 1] += 1

    w = int(input()) - 1

    queue = deque()

    for i, c in enumerate(cnts):
        if c == 0:
            queue.append(i)

    memo = weights.copy()

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            cnts[i] -= 1
            memo[i] = max(memo[i], memo[v] + weights[i])
            if cnts[i] == 0:
                queue.append(i)

        if cnts[w] == 0:
            print(memo[w])
            break
