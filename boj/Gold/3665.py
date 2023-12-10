import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [set() for _ in range(n)]
    cnts = [0] * n
    last_year = list(map(int, input().split()))

    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[last_year[i] - 1].add(last_year[j] - 1)
            cnts[last_year[j] - 1] += 1

    m = int(input())
    flag = False

    for _ in range(m):
        a, b = map(int, input().split())
        if b - 1 in graph[a - 1]:
            graph[a - 1].remove(b - 1)
            cnts[b - 1] -= 1
            graph[b - 1].add(a - 1)
            cnts[a - 1] += 1
        else:
            graph[b - 1].remove(a - 1)
            cnts[a - 1] -= 1
            graph[a - 1].add(b - 1)
            cnts[b - 1] += 1

    for c in cnts:
        if c < 0:
            print("?")
            continue

    queue = deque([i for i in range(n) if cnts[i] == 0])
    ans = []
    while queue:
        cur = queue.popleft()
        ans.append(cur + 1)
        for i in graph[cur]:
            cnts[i] -= 1
            if cnts[i] == 0:
                queue.append(i)
    if sum(cnts) == 0:
        print(*ans)
    else:
        print("IMPOSSIBLE")
