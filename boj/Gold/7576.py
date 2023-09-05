import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

visit = [
    [True for _ in range(m)] for _ in range(n)
]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

q = deque()

ex_zero = False

for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            q.append([r, c])
        elif not ex_zero and arr[r][c] == 0:
            ex_zero = True

ans = 0
t = []
while q and ex_zero:
    y, x = q.popleft()
    visit[y][x] = False
    arr[y][x] = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] and arr[ny][nx] == 0:
            visit[ny][nx] = False
            arr[ny][nx] = 1
            t.append([ny, nx])

    if not q and t:
        ans += 1
        q = deque(t)
        t = []


key = True

for i in range(n):
    for j in range(m):
        if visit[i][j] and arr[i][j] == 0:
            key = False
            break

print(ans if key else -1)
