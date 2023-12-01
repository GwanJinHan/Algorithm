from itertools import combinations_with_replacement as cmr
n, m = map(int, input().split())
arr = list(range(1, n + 1))
answers = list(cmr(arr, m))
for ans in answers:
    print(*ans)
