from itertools import permutations as pm

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answers = list(pm(arr, k))

s = set()
for ans in answers:
    t = str(ans)
    if t in s:
        continue
    print(*ans)
    s.add(t)
