import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

g = int(input())
p = int(input())
parent = [i for i in range(g)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(s1, s2):
    if s1 > s2:
        parent[s1] = s2
    else:
        parent[s2] = s1


flag = False
zero_flag = False
ans = 0
for _ in range(p):
    n = int(input()) - 1
    if flag:
        continue
    s1 = find(n)
    if s1 == 0 and zero_flag:
        flag = True
        continue
    ans += 1

    if s1 != 0:
        union(s1, s1 - 1)
    else:
        zero_flag = True

print(ans)
