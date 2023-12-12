import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(s1, s2):
    if s1 < s2:
        parent[s2] = s1
    else:
        parent[s1] = s2


for _ in range(n - 2):
    a, b = map(int, input().split())
    s1 = find(a - 1)
    s2 = find(b - 1)

    if s1 != s2:
        union(s1, s2)

for i in range(n):
    parent[i] = find(i)

a, b = set(parent)
print(a + 1, b + 1)
