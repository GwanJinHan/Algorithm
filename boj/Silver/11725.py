import sys
from collections import defaultdict as dd
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
d = dd(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

ans = {}
def search(n):
    for child in d[n]:
        if child in ans: 
            continue
        ans[child] = n
        search(child)

search(1)

for i in range(2, n + 1):
    print(ans[i])