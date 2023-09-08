n = int(input())

arr = [1, 3]

for i in range(3, n + 1):
    arr.append(arr[-2] * 2 + arr[-1])

print(arr[n - 1] % 10007)
