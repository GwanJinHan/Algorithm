from itertools import combinations as cm

n, k = map(int, input().split())
arr = list(range(1, n + 1))
arr.sort()

answers = list(cm(arr, k))

for ans in answers:
    print(*ans)
