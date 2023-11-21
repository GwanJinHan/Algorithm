import sys
input = sys.stdin.readline

n, t = map(int, input().split())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 0

citis = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        if i == j:
            continue
        elif citis[i][0] == citis[j][0] == 1:
            if t <= abs(citis[i][1] - citis[j][1]) + \
                    abs(citis[i][2] - citis[j][2]):
                matrix[i][j] = matrix[j][i] = t
            else:
                matrix[i][j] = abs(citis[i][1] - citis[j][1]) + \
                    abs(citis[i][2] - citis[j][2])
        else:
            matrix[i][j] = matrix[j][i] = abs(citis[i][1] - citis[j][1]) + \
                abs(citis[i][2] - citis[j][2])

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c or inter == r or inter == c:
                continue
            if matrix[r][c] < matrix[r][inter] + matrix[inter][c]:
                matrix[r][c] = matrix[r][inter] + matrix[inter][c]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(matrix[a - 1][b - 1])
