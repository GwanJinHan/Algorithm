import sys
input = sys.stdin.readline

n = int(input())
ys = []
xs = []

for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

start = 0
end = n - 1
height = sys.maxsize
while end < n and end - start + 1 >= n // 2:
    

