import sys
n = int(input())
arr = list(map(int, input().split()))

s = sorted(arr)

d = {}

cnt = 0
cur = None
ans = []
for val in s:
    try:
        if d[val] >= 0:
            continue
    except:
        d[val] = cnt
    cnt += 1

for v in arr:
    sys.stdout.write(f'{d[v]} ')
