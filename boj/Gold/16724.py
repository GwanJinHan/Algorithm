import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n * m)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(s1, s2):
    if s1 < s2:
        parent[s2] = s1
    else:
        parent[s1] = s2


matrix = [input().rstrip() for _ in range(n)]

for r in range(n):
    for c in range(m):
        if matrix[r][c] == "L":
            s1 = find(r * m + c)
            s2 = find(r * m + c - 1)
            if s1 != s2:
                union(s1, s2)
        elif matrix[r][c] == "R":
            s1 = find(r * m + c)
            s2 = find(r * m + c + 1)
            if s1 != s2:
                union(s1, s2)
        elif matrix[r][c] == "U":
            s1 = find(r * m + c)
            s2 = find((r - 1) * m + c)
            if s1 != s2:
                union(s1, s2)
        elif matrix[r][c] == "D":
            s1 = find(r * m + c)
            s2 = find((r + 1) * m + c)
            if s1 != s2:
                union(s1, s2)

for r in range(n):
    for c in range(m):
        if matrix[r][c] == "L":
            s1 = find(r * m + c)
            s2 = find(r * m + c - 1)
            if s1 != s2:
                union(s1, s2)
        elif matrix[r][c] == "R":
            s1 = find(r * m + c)
            s2 = find(r * m + c + 1)
            if s1 != s2:
                union(s1, s2)
        elif matrix[r][c] == "U":
            s1 = find(r * m + c)
            s2 = find((r - 1) * m + c)
            if s1 != s2:
                union(s1, s2)
        elif matrix[r][c] == "D":
            s1 = find(r * m + c)
            s2 = find((r + 1) * m + c)
            if s1 != s2:
                union(s1, s2)

print(len(set(parent)))
