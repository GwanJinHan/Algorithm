import sys
import math
input = sys.stdin.readline

MIN, MAX = map(int, input().split())

arr = [True] * (MAX - MIN + 1)

for d in range(2, int(math.sqrt(MAX)) + 1):
    square = d ** 2

    if square > MAX:
        break

    m = (MIN // square) + 1 if MIN % square != 0 else (MIN // square)

    for i in range(m * square, MAX + 1, square):
        arr[i - 1 - MIN] = False

cnt = 0
for val in arr:
    if val:
        cnt += 1

print(cnt)
