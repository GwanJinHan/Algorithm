import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n)]


def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])


def union(s1, s2):
    if s1 < s2:
        parent[s2] = s1
    else:
        parent[s1] = s2


ans = 0
flag = False
for i in range(m):
    a, b = map(int, input().split())
    if flag:
        continue
    s1 = find(a)
    s2 = find(b)

    if s1 != s2:
        union(s1, s2)
    else:
        ans = i + 1
        flag = True
print(ans)
