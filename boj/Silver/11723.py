import sys
input = sys.stdin.readline

n = int(input())

S = set()
for _ in range(n):
    method, *x = input().split()
    x = int(*x)

    if method == "add":
        S.add(x)
    elif method == "remove":
        try:
            S.remove(x)
        except:
            pass
    elif method == "check":
        print(1 if x in S else 0)
    elif method == "toggle":
        try:
            S.remove(x)
        except:
            S.add(x)
    elif method == "all":
        S = set(range(1, 21))
    elif method == "empty":
        S.clear()
