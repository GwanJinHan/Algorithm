a, b = map(int, input().split())

arr = []
i = 1
while i <= b:
    for _ in range(i):
        arr.append(i)
    i += 1

print(sum(arr[a - 1: b]))
