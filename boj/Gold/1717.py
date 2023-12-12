import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(s1, s2):
    if s1 > s2:
        parent[s1] = s2
    else:
        parent[s2] = s1


for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 0:
        s1 = find(b)
        s2 = find(c)
        if s1 != s2:
            union(s1, s2)

    else:
        s1 = find(b)
        s2 = find(c)
        print("YES" if s1 == s2 else "NO")
