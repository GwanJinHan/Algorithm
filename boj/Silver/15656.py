from itertools import product as pd

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answers = list(pd(arr, repeat=k))

for ans in answers:
    print(*ans)
