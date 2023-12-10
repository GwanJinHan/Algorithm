import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
cnts = [0] * n

for _ in range(m):
    arr = list(map(int, input().split()))[1:]

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            graph[arr[i] - 1].append(arr[j] - 1)
            cnts[arr[j] - 1] += 1

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
    for a in ans:
        print(a)
else:
    print(0)
