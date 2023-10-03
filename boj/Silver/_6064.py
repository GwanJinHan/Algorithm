import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cnt = 1
    m, n, x, y = map(int, input().split())
    cur_x, cur_y = 1, 1
    flag = False

    while True:
        if cur_x == x and cur_y == y:
            break
        cnt += 1

        if cur_y == n:
            cur_y = 1
        else:
            cur_y += 1

        if cur_x == m:
            cur_x = 1
        else:
            cur_x += 1

        if cur_x == 1 and cur_y == 1:
            cnt = -1
            break

    print(cnt)
