import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c:
                continue
            if arr[r][c] > arr[r][inter] + arr[inter][c]:
                arr[r][c] = arr[r][inter] + arr[inter][c]

for _ in range(m):
    a, b, c = map(int, input().split())

    if arr[a - 1][b - 1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
