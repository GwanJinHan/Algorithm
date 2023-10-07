import sys
input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    u = list(map(int, input().split()))
    d = list(map(int, input().split()))
    pre_u = u[0]
    pre_d = d[0]

    for i in range(1, n):
        if i == 1:
            post_u = pre_d + u[i]
            post_d = pre_u + d[i]
        else:
            t1, t2 = post_u, post_d
            post_u, post_d = u[i] + \
                max(post_d, pre_d), d[i] + max(post_u, pre_u)
            pre_u, pre_d = t1, t2

    ans.append(max(pre_d, pre_u) if n == 1 else max(post_d, post_u))

for val in ans:
    print(val)
