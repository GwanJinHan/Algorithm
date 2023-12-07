import sys
input = sys.stdin.readline

n = int(input())
planets = [tuple(map(int, input().split())) for _ in range(n)]

temp_edges = []
for i in range(n - 1):
    for j in range(i + 1, n):
        temp_edges.append((i, j, min(abs(planets[i][0] - planets[j][0]), abs(planets[i][1] - planets[j][1]), abs(
            planets[i][2] - planets[j][2])), planets[i][0] - planets[j][0], planets[i][1] - planets[j][1], planets[i][2] - planets[j][2]))

edges = []

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


planets.sort(key=lambda x: x[2])

ans = 0

for v1, v2, dist in edges:
    if find(v1) != find(v2):
        ans += dist
        union(find(v1), find(v2))

print(planets)
