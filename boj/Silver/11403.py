import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 0 and arr[r][inter] and arr[inter][c]:
                arr[r][c] = 1

for val in arr:
    print(*val)
