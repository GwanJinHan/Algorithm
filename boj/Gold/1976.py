import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

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


for r in range(n):
    t = list(map(int, input().split()))
    for c in range(n):
        if t[c] == 1:
            s1 = find(r)
            s2 = find(c)
            if s1 != s2:
                union(s1, s2)

arr = list(map(int, input().split()))
ans = set([parent[a - 1] for a in arr])

print("YES" if len(ans) == 1 else "NO")
