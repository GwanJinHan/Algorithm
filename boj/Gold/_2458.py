import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    