import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for zero_r in range(n):
    for zero_c in range(m):
        if arr[zero_r][zero_c] == 0:
            visit = [[False] * m for _ in range(n)]
            queue = deque([(zero_r, zero_c)])
            cnt = 0

            while queue:
                r, c = queue.popleft()

                if visit[r][c]:
                    continue
                visit[r][c] = True
                cnt += 1

                for i in range(4):
                    nr, nc = r + dy[i], c + dx[i]

                    if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc] and arr[nr][nc] == 0:
                        queue.append((nr, nc))

            for i in range(n):
                for j in range(m):
                    if visit[i][j]:
                        arr[i][j] = - cnt
ans = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if arr[y][x] == 1:
            cnt = 0
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] <= 0:
                    cnt += arr[ny][nx]
            ans[y][x] = - (cnt - 1) % 10

for a in ans:
    for b in a:
        print(b, end="")
    print()
