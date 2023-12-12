import sys
input = sys.stdin.readline


def find(x):
    global parent
    global cnts
    if x not in parent:
        parent[x] = x
        cnts[x] = 1
        return x
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(s1, s2):
    global parent
    global cnts
    if s1 < s2:
        parent[s2] = s1
        cnts[s1] += cnts[s2]
        return cnts[s1]
    else:
        parent[s1] = s2
        cnts[s2] += cnts[s1]
        return cnts[s2]


t = int(input())
for _ in range(t):
    n = int(input())
    parent = {}
    cnts = {}

    for _ in range(n):
        a, b = input().rstrip().split()

        s1 = find(a)
        s2 = find(b)

        if s1 != s2:
            cnt = union(s1, s2)
            print(cnt)
        else:
            print(cnts[s1])
