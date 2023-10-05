from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [
    list(map(int, list(input().rstrip()))) for _ in range(n)
]

visited = [[[False, False]
            for _ in range(m)] for _ in range(n)]  # 벽 깬 사람, 벽 안 깬 사람

queue = deque([(0, 0, 1, True)])

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ans = sys.maxsize
while queue:
    r, c, cnt, flag = queue.popleft()
    if r == n - 1 and c == m - 1:
        ans = min(ans, cnt)
        break

    if (visited[r][c][0] and not flag) or visited[r][c][1]:
        continue
    visited[r][c][0] = True
    if flag:  # 벽 안 깬 사람도 지나갔으면 True로
        visited[r][c][1] = True

    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]

        if 0 <= nr < n and 0 <= nc < m:
            if flag:  # 벽 안 깬 사람
                if arr[nr][nc] == 1 and not visited[nr][nc][0]:
                    queue.append((nr, nc, cnt + 1, False))
                elif arr[nr][nc] == 0 and not visited[nr][nc][1]:
                    queue.append((nr, nc, cnt + 1, flag))

            else:  # 벽 깬 사람
                if arr[nr][nc] == 0 and not visited[nr][nc][0]:
                    queue.append((nr, nc, cnt + 1, flag))

print(ans if ans != sys.maxsize else -1)
