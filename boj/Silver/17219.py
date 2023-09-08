import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}

for _ in range(n):
    a, p = input().rstrip().split()
    d[a] = p

ans = []
for _ in range(m):
    s = input().rstrip()
    ans.append(d[s])


for val in ans:
    print(val)
