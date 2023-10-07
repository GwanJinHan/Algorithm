import sys
input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    u = list(map(int, input().split()))
    d = list(map(int, input().split()))
    dp_u = [u[0]]
    dp_d = [d[0]]

    for i in range(1, n):
        if i == 1:
            dp_d.append(u[0] + d[1])
            dp_u.append(d[0] + u[1])
        else:
            dp_d.append(max(dp_u[i - 2], dp_u[i - 1]) + d[i])
            dp_u.append(max(dp_d[i - 2], dp_d[i - 1]) + u[i])

    ans.append(max(dp_d[-1], dp_u[-1]))

for val in ans:
    print(val)
