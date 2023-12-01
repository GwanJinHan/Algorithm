from itertools import combinations_with_replacement as cmr

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answers = list(cmr(arr, k))

for ans in answers:
    print(*ans)
