import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [
    list(map(int, input().rstrip())) for _ in range(n)
]
visited = [[False] * m for _ in range(n)]
queue = deque([(0, 0, 1)])

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]


while queue:
    y, x, path = queue.popleft()
    if visited[y][x]:
        continue
    if y == n - 1 and x == m - 1:
        print(path)
        break

    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1 and not visited[ny][nx]:
            queue.append((ny, nx, path + 1))
