import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] * (k + 1)

for _ in range(n):
    w, v = map(int, input().split())
