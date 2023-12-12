import sys
input = sys.stdin.readline

n = int(input())
planets = [[i] + list(map(int, input().split())) for i in range(n)]

edges = []
x = sorted(planets, key=lambda x: x[1])
for i in range(n - 1):
    edges.append((x[i][0], x[i + 1][0],
                 x[i + 1][1] - x[i][1]))
y = sorted(planets, key=lambda x: x[2])
for i in range(n - 1):
    edges.append((y[i][0], y[i + 1][0],
                 y[i + 1][2] - y[i][2]))
z = sorted(planets, key=lambda x: x[3])
for i in range(n - 1):
    edges.append((z[i][0], z[i + 1][0],
                 z[i + 1][3] - z[i][3]))

parent = [i for i in range(n)]


def find(idx):
    if parent[idx] != idx:
        parent[idx] = find(parent[idx])
    return parent[idx]


def union(s1, s2):
    if s1 < s2:
        parent[s2] = s1
    else:
        parent[s1] = s2


edges.sort(key=lambda x: x[2])

ans = 0

for v1, v2, dist in edges:
    s1 = find(v1)
    s2 = find(v2)
    if s1 != s2:
        ans += dist
        union(s1, s2)

print(ans)
