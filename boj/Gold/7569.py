# https://www.acmicpc.net/source/65692337

from collections import deque
import sys

# m : 가로(col), n : 세로(row), h: 높이
m, n, h = map(int, sys.stdin.readline().split())
arr = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)
]

visit = [
    [[True for _ in range(m)] for _ in range(n)] for _ in range(h)
]

dz, dy, dx = [0, 0, 0, 0, 1, -1], [0, 1, 0, -
                                   1, 0, 0], [1, 0, -1, 0, 0, 0]  # 동남서북 위아래

q = deque()

zero_existence = False

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i, j, k])
                visit[i][j][k] = False
            elif not zero_existence and arr[i][j][k] == 0:
                zero_existence = True

t = deque()
ans = 0
while q and zero_existence:
    z, y, x = q.popleft()

    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]

        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and visit[nz][ny][nx] and arr[nz][ny][nx] == 0:
            t.append([nz, ny, nx])
            visit[nz][ny][nx] = False
            arr[nz][ny][nx] = 1

    if not q and t:
        q = t.copy()
        t = deque()
        ans += 1

existence_left_zero = False

if zero_existence:
    for floor in arr:
        for row in floor:
            if 0 in row:
                existence_left_zero = True
                break

print(-1 if existence_left_zero else ans)
