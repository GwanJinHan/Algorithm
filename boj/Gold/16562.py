import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
friends_fee = list(map(int, input().split()))
parents = [i for i in range(n)]


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(s1, s2):
    if friends_fee[s1] > friends_fee[s2]:
        parents[s1] = s2
    else:
        parents[s2] = s1


for _ in range(m):
    a, b = map(int, input().split())
    s1 = find(a - 1)
    s2 = find(b - 1)

    if s1 != s2:
        union(s1, s2)

for i in range(n):
    parents[i] = find(i)

total = 0
for t in set(parents):
    total += friends_fee[t]

if total <= k:
    print(total)
else:
    print("Oh no")
