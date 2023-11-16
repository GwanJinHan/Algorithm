import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [
    list(map(int, input().split())) for _ in range(n)
]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

ans = 0
while True:
    flag = False
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:

                queue = deque([(r, c)])
                visit = [[False] * m for _ in range(n)]
                melted = []
                while queue:
                    y, x = queue.popleft()

                    if visit[y][x]:
                        continue
                    visit[y][x] = True

                    cnt = 0
                    for i in range(4):
                        ny, nx = y + dy[i], x + dx[i]
                        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 1 and not visit[ny][nx]:
                            queue.append((ny, nx))
                        elif 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 0:
                            cnt += 1

                    if cnt >= 2:
                        melted.append((y, x))

                for mr, mc in melted:
                    matrix[mr][mc] = 0
                ans += 1
                flag = True
                break
        if flag:
            break
    if not flag:
        break

print(ans)
