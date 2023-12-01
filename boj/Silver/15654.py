from itertools import permutations as pm

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answers = list(pm(arr, k))

for ans in answers:
    print(*ans)
