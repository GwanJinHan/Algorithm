import sys
input = sys.stdin.readline


arr = []

n = int(input())
for _ in range(n):
    a, b, c, d = input().split()
    b, c, d = map(int, [b, c, d])
    arr.append((d, c, b, a))

arr.sort()

print(arr[-1][3])
print(arr[0][3])
