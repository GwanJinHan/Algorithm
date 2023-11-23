from collections import  deque

n = int(input())
arr = list(map(int, input().split()))
d = int(input())

m = [[] for _ in range(n)]
for num, val in enumerate(arr):
    if val == -1:
        root = num
    else:
        m[val].append(num)

stack = deque([root])
ans = 0

while stack:
    t = stack.pop()

    if t == d:
        continue

    if len(m[t]) == 0 or (len(m[t]) == 1 and m[t][0] == d):
        ans += 1
    else:
        stack.extend(m[t])

print(ans)