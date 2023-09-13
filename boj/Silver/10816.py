import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

d = {}

for val in a:
    try:
        d[val] += 1
    except:
        d[val] = 1
ans = []
for tar in b:
    try:
        ans.append(d[tar])
    except:
        ans.append(0)

print(*ans)
