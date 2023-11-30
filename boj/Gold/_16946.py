import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
ans = [a.copy() for a in arr]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
num = 0
for zero_r in range(n):
    for zero_c in range(m):
        if arr[zero_r][zero_c] == 0:
            num += 1
            visit = [[False] * m for _ in range(n)]
            queue = deque([(zero_r, zero_c)])
            cnt = 0
            one_list = []

            while queue:
                r, c = queue.popleft()

                if visit[r][c]:
                    continue
                visit[r][c] = True
                arr[r][c] = -1
                cnt += 1

                for i in range(4):
                    nr, nc = r + dy[i], c + dx[i]

                    if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc] and arr[nr][nc] == 0:
                        queue.append((nr, nc))

                    elif 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                        one_list.append((nr, nc))

            for y, x in one_list:
                if not visit[y][x]:
                    ans[y][x] += cnt
                    visit[y][x] = True

for a in ans:
    for b in a:
        if b > 0:
            b = b % 10
        print(b, end="")
    print()
