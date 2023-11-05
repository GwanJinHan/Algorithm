n = int(input())
arr = list(map(int, input().split()))

asc = [1] * n
des = [1] * n + [0]
des_max = [0] * (n + 1)
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            asc[i] = max(asc[i], asc[j] + 1)


for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            des[i] = max(des[i], des[j] + 1)
    des_max[i + 1] = max(des_max[i], des[i])

ans = 0
m = max(des)
for i in range(n):
    ans = max(ans, asc[i] + des_max[i + 1] - des[i] + 1)

print(ans)
print(asc)
print(des)
print(des_max)
