import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(input().rstrip()) for _ in range(n)
]
visit = [
    [True for _ in range(n)] for _ in range(n)
]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]  # 북동남서

cnt = 0
D_cnt = 0


def dfs(y, x, prev):
    stack = [(y, x)]
    visit[y][x] = False
    if arr[y][x] == 'R' or arr[y][x] == 'G':
        arr[y][x] = 'X'
    while stack:
        y, x = stack.pop()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny >= 0 and ny < n and nx >= 0 and nx < n and visit[ny][nx] and arr[ny][nx] == prev:
                if arr[ny][nx] == 'R' or arr[ny][nx] == 'G':
                    arr[ny][nx] = 'X'
                stack.append((ny, nx))
                visit[ny][nx] = False


for r in range(n):
    for c in range(n):
        if visit[r][c]:
            dfs(r, c, arr[r][c])
            cnt += 1

visit = [
    [True for _ in range(n)] for _ in range(n)
]


for r in range(n):
    for c in range(n):
        if visit[r][c]:
            dfs(r, c, arr[r][c])
            D_cnt += 1

print(cnt, D_cnt)
