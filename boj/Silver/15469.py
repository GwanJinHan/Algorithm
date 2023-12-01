from itertools import permutations as pm
n, m = map(int, input().split())
arr = list(range(1, n + 1))
answers = list(pm(arr, m))
for ans in answers:
    print(*ans)
