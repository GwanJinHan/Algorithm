from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

arr = [
    list(map(int, input().rstrip())) for _ in range(n)
]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

visited = [[False] * n for _ in range(n)]

queue = deque()
ans = []

for r in range(n):
    for c in range(n):

        if arr[r][c] == 0 or visited[r][c]:
            continue

        queue.append((r, c))
        cnt = 0
        while queue:
            y, x = queue.popleft()
            if visited[y][x]:
                continue
            else:
                visited[y][x] = True

            cnt += 1

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 1 and not visited[ny][nx]:
                    queue.append((ny, nx))

        ans.append(cnt)

ans.sort()
print(len(ans))
for val in ans:
    print(val)
