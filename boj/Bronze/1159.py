import sys
input = sys.stdin.readline

d = dict()
n = int(input())
for _ in range(n):
    s = input().rstrip()
    try:
        d[s[0]] += 1
    except:
        d[s[0]] = 1

keys = list(d.keys())
keys.sort()

ans = []
for key in keys:
    if d[key] >= 5:
        ans.append(key)

if len(ans) == 0:
    print("PREDAJA")
else:
    print("".join(ans))
