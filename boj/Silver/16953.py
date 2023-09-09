a, b = map(int, input().split())
cnt = 0
while a != b:
    if b % 10 == 1 and b != 1:
        cnt += 1
        b //= 10
    elif b % 2 == 0:
        cnt += 1
        b //= 2
    else:
        cnt = -2
        break

print(cnt + 1)
