import sys
input = sys.stdin.readline

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((i, j, (abs(
            stars[i][0] - stars[j][0]) ** 2 + abs(stars[i][1] - stars[j][1]) ** 2) ** 0.5))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(n)]


def find(idx):
    global parent
    while parent[idx] != idx:
        idx = parent[idx]

    return idx


def union(s1, s2):
    if s1 < s2:
        parent[s1] = s2
    else:
        parent[s2] = s1


ans = 0
for v1, v2, dist in edges:
    s1 = find(v1)
    s2 = find(v2)

    if s1 != s2:
        ans += dist
        union(s1, s2)

print(ans)
