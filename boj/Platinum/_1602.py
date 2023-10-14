import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
dogs = list(map(int, input().split()))

fw = [[sys.maxsize] * n for _ in range(n)]
dt = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b, d = map(int, input().split())

    fw[a - 1][b - 1] = d
    fw[b - 1][a - 1] = d

    dt[a - 1][b - 1] = max(dogs[a - 1], dogs[b - 1])
    dt[b - 1][a - 1] = max(dogs[a - 1], dogs[b - 1])

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c:
                fw[r][c] = 0
            elif fw[r][c] + dt[r][c] > fw[r][inter] + fw[inter][c] + max(dt[inter][c], dt[r][inter]):
                fw[r][c] = fw[r][inter] + fw[inter][c]
                dt[r][c] = max(dt[inter][c], dt[r][inter])

for _ in range(q):
    a, b = map(int, input().split())
    if fw[a - 1][b - 1] == sys.maxsize:
        print(-1)
    else:
        print(fw[a - 1][b - 1] + dt[a - 1][b - 1])

print(fw)
print(dt)
