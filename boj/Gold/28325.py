import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
cur_zero = 0

if all(val == 1 for val in arr):
    cnt = n

elif all(val == 0 for val in arr):
    cnt = n // 2

else:
    first_zero = 0
    first = True

    for val in arr:
        if val == 0:
            if first:
                first_zero += 1
            else:
                cur_zero += 1
        else:
            if first:
                first = False
            cnt += val + (cur_zero + 1) // 2
            cur_zero = 0

    cnt += (cur_zero + first_zero + 1) // 2

print(cnt)
