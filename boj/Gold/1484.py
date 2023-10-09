g = int(input())

cur = 1
rem = 1
t_g = 0
ans = []
while cur ** 2 - (cur - 1) ** 2 <= g:
    t_g = cur ** 2 - rem ** 2
    if t_g < g:
        cur += 1
    elif t_g > g:
        rem += 1
    else:
        ans.append(cur)
        rem += 1

if len(ans) == 0:
    print(-1)
else:
    for a in ans:
        print(a)
