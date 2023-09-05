from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
arr = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    if a not in arr[b] and b not in arr[a]:
        arr[a].append(b)
        arr[b].append(a)

for val in arr:
    val.sort()


b_ans = []

queue = deque([v])
visit = [True for _ in range(n)]

while queue:
    q = queue.popleft()
    visit[q - 1] = False
    b_ans.apend(q)

    for val in arr[q - 1]:
        if visit[val - 1]:
            queue.append(val)


queue = deque([v])
visit = [True for _ in range(n)]
d_ans = []

while queue:
    q = queue.popleft()
    visit[q - 1] = False
    d_ans.append(q)

    for val in arr[q - 1]:
        if visit[val - 1]:
            queue.append(val)



print(d_ans)
print(b_ans)