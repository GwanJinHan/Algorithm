import sys
from heapq import heappop, heappush
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

matrix = [[sys.maxsize] * v for _ in range(v)]
visit = [True] + [False] * (v - 1)

for i in range(v):
    matrix[i][i] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    matrix[a - 1][b - 1] = c
    matrix[b - 1][a - 1] = c
