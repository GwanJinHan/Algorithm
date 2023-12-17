import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = sys.maxsize

parent = [i for i in range(n)]
matrix = [[INF] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(s1, s2):
    if s1 < s2:
        parent[s2] = s1
    else:
        parent[s1] = s2


for _ in range(m):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = 1

    s1 = find(a - 1)
    s2 = find(b - 1)

    if s1 != s2:
        union(s1, s2)

for i in range(n):
    parent[i] = find(i)

for k in range(n):
    for r in range(n):
        for c in range(n):
            matrix[r][c] = min(matrix[r][c], matrix[r][k] + matrix[k][c])

d = {}

for i, val in enumerate(parent):
    try:
        d[val].append(i)
    except:
        d[val] = [i]


print(len(set(parent)))
a = []
for key, arr in d.items():
    if len(arr) == 1:
        a.append(key + 1)
    else:
        t = INF
        ans = 0
        for i in range(len(arr)):
            acc = 0
            for j in range(len(arr)):
                if i == j:
                    continue
                acc = max(acc, matrix[arr[i]][arr[j]])
            if acc < t:
                t = acc
                ans = arr[i] + 1
        a.append(ans)
a.sort()
for v in a:
    print(v)
