n = int(input())

cnt = 0

if n % 3 == 0:
    cnt = n // 3 - 1
elif n % 3 == 1:
    cnt = n // 3
else:
    if (n - 2) // 3 % 2 == 0:
        cnt = (n // 6) + 1
    else:
        cnt = (n // 3) + 1

print(cnt)
