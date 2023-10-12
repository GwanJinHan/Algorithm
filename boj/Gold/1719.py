import sys
input = sys.stdin.readline

n, m = map(int, input().split())

inters = [["-"] * n for _ in range(n)]  # 최단거리 경로 번호표
fw = [[sys.maxsize] * n for _ in range(n)]  # 최단거리 표

for _ in range(m):
    a, b, time = map(int, input().split())

    fw[a - 1][b - 1] = time
    fw[b - 1][a - 1] = time
    inters[a - 1][b - 1] = b
    inters[b - 1][a - 1] = a

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c or r == inter or c == inter:
                continue

            if fw[r][c] > fw[r][inter] + fw[inter][c]:
                fw[r][c] = fw[r][inter] + fw[inter][c]
                inters[r][c] = inters[r][inter] if inters[r][inter] != "-" else inter + 1

for i in inters:
    print(*i)
