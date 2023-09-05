import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)
op = [list(map(int, input().split())) for _ in range(m)]
s = 0

for i, val in enumerate(arr):
    s += arr[i]
    arr[i] = s

for a, b in op:
    print(arr[b] - arr[a - 1])
