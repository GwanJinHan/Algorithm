n = int(input())
arr = list(input().split())
m = 0
for a in arr:
    m = max(m, len(a))
arr.sort(key=lambda x: x * m, reverse=True)

print(int("".join(arr)))
