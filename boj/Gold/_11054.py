n = int(input())
arr = list(map(int, input().split()))

asc = [1] * n
des = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            asc[i] = max(asc[i], asc[j] + 1)


for i in range(n - 1, -1, -1):
    for j in range(n - 1, n - i - 1, -1):
        if arr[j] < arr[i]:
            des[i] = max(des[i], des[j] + 1)

ans = 0
for i in range(n - 1):
    ans = max(ans, asc[i] + des[i + 1])

print(ans)

print(asc)
print(des)
