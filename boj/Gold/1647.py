import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]
edges = []

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    edges.append((v1 - 1, v2 - 1, cost))

edges.sort(key=lambda x: x[2])


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


ans = 0
key = -1
for v1, v2, cost in edges:
    s1 = find(v1)
    s2 = find(v2)

    if s1 != s2:
        ans += cost
        key = max(key, cost)
        union(s1, s2)

print(ans - key)
