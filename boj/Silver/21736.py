import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
queue = deque()
for i in range(n):
    t = input().rstrip()
    if "I" in t:
        queue.append((t.index("I"), i))

    arr.append(list(t))

visited = [[False] * m for _ in range(n)]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
ans = 0
while queue:
    x, y = queue.popleft()

    if visited[y][x]:
        continue

    if arr[y][x] == "P":
        ans += 1

    visited[y][x] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx] != "X":

            queue.append((nx, ny))


print(ans if ans != 0 else "TT")
