n = int(input())

start = 1
end = 2
cur = 1
cnt = 0
while start < end:
    if cur > n:
        cur -= start
        start += 1
    elif cur < n:
        cur += end
        end += 1
    else:
        cnt += 1
        cur += end
        end += 1

print(cnt)
