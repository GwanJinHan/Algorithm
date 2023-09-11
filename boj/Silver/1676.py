n = int(input())

ans = 1

for i in range(1, n + 1):
    ans *= i
cnt = 0
for s in str(ans)[::-1]:
    if s != '0':
        break
    cnt += 1

print(cnt)
