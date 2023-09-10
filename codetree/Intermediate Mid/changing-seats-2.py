import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [set([i]) for i in range(1, n + 1)]  # 사람 기준
cur = [i for i in range(1, n + 1)]

cmds = [list(map(int, input().split()))for _ in range(k)]
for i in range(k * 3):
    a, b = cmds[i % k]
    cur[a - 1], cur[b - 1] = cur[b - 1], cur[a - 1]

    arr[cur[a - 1] - 1].add(a)
    arr[cur[b - 1] - 1].add(b)

for e in arr:
    print(len(e))
