from itertools import combinations as cm

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answers = list(cm(arr, k))

for ans in answers:
    print(*ans)
