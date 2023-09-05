n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def check_around(cur_r, cur_c, arr):
    for i in range(4):
        ny, nx = cur_r + dy[i], cur_c + dx[i]
        if arr[ny][nx] == 0:
            return True
    return False


cur_r = r
cur_c = c
cur_d = d

cnt = 0

while True:
    if arr[cur_r][cur_c] == 0:
        arr[cur_r][cur_c] = -1
        cnt += 1

    if check_around(cur_r, cur_c, arr):
        cur_d = (cur_d + 3) % 4
        ny, nx = cur_r + dy[cur_d], cur_c + dx[cur_d]
        if arr[ny][nx] == 0:
            cur_r, cur_c = ny, nx

    else:
        back = (cur_d + 2) % 4
        ny, nx = cur_r + dy[back], cur_c + dx[back]
        if arr[ny][nx] != 1:
            cur_r, cur_c = ny, nx
        else:
            break

print(cnt)
