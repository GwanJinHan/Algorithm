# 일명 신발끈 공식 이용
import sys
input = sys.stdin.readline

n = int(input())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)


ans = 0
for i in range(n):
    ans += (xs[i] + xs[(i + 1) % n]) * (ys[i] - ys[(i + 1) % n])

print(round(abs(ans) / 2, 2))
