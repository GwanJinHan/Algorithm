# deque 와 list 의 차이점 명심!

import sys
input = sys.stdin.readline
t = int(input())


dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]


def dfs(m, n, arr, one_list):
    cnt = 0
    visit = [[True for _ in range(m)] for _ in range(n)]

    while one_list:
        r, c = one_list.pop()
        if visit[r][c]:
            queue = [[r, c]]

            while queue:
                row, column = queue.pop()
                visit[row][column] = False
                for i in range(4):
                    nx, ny = column + dx[i], row + dy[i]

                    if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1 and visit[ny][nx]:
                        queue.append([ny, nx])
            cnt += 1

    return cnt


ans = []
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    one_list = []
    for _ in range(k):
        x, y = map(int, input().split())
        one_list.append([y, x])
        arr[y][x] = 1
    ans.append(dfs(m, n, arr, one_list))

for val in ans:
    print(val)
