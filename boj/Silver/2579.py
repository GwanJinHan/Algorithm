import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

acc = [(0, 0, 0), (arr[0], arr[0], 0), (arr[1], arr[0] + arr[1], 0)
       ] if n != 1 else [(0, 0, 0), (arr[0], arr[0], 0)]

if n > 2:
    acc.append((arr[0] + arr[2], arr[1] + arr[2], 0))

for i in range(3, n):
    acc.append((
        max(acc[i - 2][0], acc[i - 2][2]) + arr[i - 2] + arr[i],
        max(acc[i - 2]) + arr[i - 1] + arr[i],
        max(acc[i - 3]) + arr[i - 2] + arr[i]
    ))

print(max(acc[-1]))
