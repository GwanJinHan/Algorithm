num = int(input())
cnt = 0

while num != 0:
    num -= int(num ** 0.5) ** 2
    cnt += 1

print(cnt)
