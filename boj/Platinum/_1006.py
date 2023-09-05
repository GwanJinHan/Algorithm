# 성공 x

import sys
input = sys.stdin.readline

t = int(input())

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]  # 북동남서

for _ in range(t):
    n, w = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(2)]

    assembles = []

    for r in range(2):
        for c in range(n):

            for i in range(1, 3):
                if r == 1 and i == 2:
                    continue
                ny, nx = r + dy[i], (c + dx[i]) % n

                if arr[r][c] + arr[ny][nx] <= w:
                    assembles.append([r * n + c, ny * n + nx])

    queue = [assembles[0]]
    t = []
    visit = [[True for _ in range(n)] for _ in range(2)]
    cnt = 0
    while queue:
        cnt += 1
        for a, b in queue:
            if not visit[a // n][a % n]:
                t.append()
                visit[a // n][a % n] = True


print(assembles)


# 2차원 => 1차원으로 만들어버리기
# 시작을 아무 영향 주지 않는 곳으로 (안 겹친 곳) => 딕셔너리로 관리
# => 안 겹치는 곳 없으면 겹쳐있는 경우들이 가장 적은 곳
