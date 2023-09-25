import sys
input = sys.stdin.readline

t = int(input())

arr = []
for _ in range(t):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key = lambda x : (x[1], x[0]))
pre = arr[0][1]
cnt = 1

for s, e in arr[1:]:
    if pre <= s:
        cnt += 1
        pre = e

print(cnt)