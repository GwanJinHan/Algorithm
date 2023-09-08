import sys
input = sys.stdin.readline

t = int(input())

ans = []

arr = [1, 1, 1]
for _ in range(t):
    num = int(input())

    if num > len(arr):
        for i in range(len(arr), num):
            arr.append(arr[i - 3] + arr[i - 2])

    ans.append(arr[num - 1])

for val in ans:
    print(val)
