import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nametonum = dict()
numtoname = dict()

for i in range(1, n + 1):
    name = input().rstrip()
    nametonum[name] = i
    numtoname[i] = name

ans = []
for _ in range(m):
    k = input().rstrip()
    if k.isdigit():
        ans.append(numtoname[int(k)])
    else:
        ans.append(nametonum[k])

for val in ans:
    print(val)
