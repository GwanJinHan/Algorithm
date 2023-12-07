import sys
input = sys.stdin.readline


def find(idx):
    global parent
    while parent[idx] != idx:
        idx = parent[idx]
    return idx


def union(s1, s2):
    if s1 < s2:
        parent[s2] = s1
    else:
        parent[s1] = s2


n = int(input())
m = int(input())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(n)]

ans = 0
for v1, v2, cost in edges:
    s1 = find(v1)
    s2 = find(v2)

    if s1 != s2:
        ans += cost
        union(s1, s2)

print(ans)
