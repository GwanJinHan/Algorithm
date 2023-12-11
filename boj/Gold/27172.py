from collections import defaultdict as dd
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

t_arr = sorted(arr)
scores = dd(int)
s = set(arr)

for num in t_arr:
    if num == 1:
        continue
    for i in range(num * 2, t_arr[-1] + 1, num):
        if i in s:
            scores[num] += 1
            scores[i] -= 1

if 1 in s:
    scores[1] = n - 1
    for num in t_arr:
        if num != 1:
            scores[num] -= 1

for num in arr:
    print(scores[num], end=" ")
