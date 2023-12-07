import sys
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v)]
e_list = []


def find(idx):
    global parent
    while parent[idx] != idx:
        idx = parent[idx]
    return idx


def union(s1, s2):
    if s2 < s1:
        parent[s1] = s2
    else:
        parent[s2] = s1


for _ in range(e):
    a, b, c = map(int, input().split())
    e_list.append((a - 1, b - 1, c))

e_list.sort(key=lambda x: x[2])
ans = 0

for v1, v2, cost in e_list:
    uset = find(v1)
    vset = find(v2)

    if uset != vset:
        ans += cost
        union(uset, vset)

print(ans)
