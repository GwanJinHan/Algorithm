import sys
input = sys.stdin.readline

n = int(input())

ans = []
S = set()
for _ in range(n):
    method = input().split()

    m = method[0]
    x = -1 if m == 'all' or m == 'empty' else method[1]

    if m == "add":
        S.add(int(x))
    elif m == "remove":
        if int(x) in S:
            S.remove(int(x))
    elif m == "check":
        ans.append(1 if int(x) in S else 0)
    elif m == "toggle":
        if int(x) in S:
            S.remove(int(x))
        else:
            S.add(int(x))
    elif m == "all":
        S = set(range(1, 21))
    elif m == "empty":
        S.clear()

for val in ans:
    print(val)
