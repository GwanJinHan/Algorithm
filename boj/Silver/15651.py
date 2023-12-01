from itertools import product as pd
n, m = map(int, input().split())
arr = list(range(1, n + 1))
answers = list(pd(arr, repeat=m))
for ans in answers:
    print(*ans)
