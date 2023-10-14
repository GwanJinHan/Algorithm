import sys
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
arr = [[float('inf') for _ in range(n)] for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = -1
    arr[b - 1][a - 1] = 1

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if arr[r][c] != 0:
                continue

            elif arr[r][inter] == 1 and arr[inter][c] == 1:
                arr[r][c] = 1
            elif arr[r][inter] == -1 and arr[inter][c] == -1:
                arr[r][c] = -1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if arr[a - 1][b - 1] == float('inf'):
        print("0\n")
    else:
        print(str(arr[a - 1][b - 1]) + "\n")
