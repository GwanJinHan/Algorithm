import sys
input = sys.stdin.readline

r, c = map(int, input().split())  # 세로 가로
arr = []

s_r, s_c = 0, 0

for i in range(r):
    t = list(map(int, input().split()))
    if 2 in t:
        s_r, s_c = i, t.index(2)
    arr.append(t)

distances = [[-1 for _ in range(c)] for _ in range(r)]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

queue = [[s_r, s_c]]
dis = 0
while queue:
    t = []
    for row, col in queue:
        distances[row][col] = dis
        for i in range(4):
            ny, nx = row + dy[i], col + dx[i]
            if 0 <= ny < r and 0 <= nx < c and arr[ny][nx] == 1 and distances[ny][nx] == -1:
                distances[ny][nx] = 0
                t.append([ny, nx])
    dis += 1
    queue = t.copy()

for i, val in enumerate(distances):
    for j, v in enumerate(val):
        if v == -1:
            val[j] = 0 if arr[i][j] == 0 else -1
    print(*val)
