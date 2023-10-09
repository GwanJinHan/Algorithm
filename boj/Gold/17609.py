import sys
input = sys.stdin.readline
t = int(input())
ans = []
for _ in range(t):
    s = input().rstrip()
    start = 0
    end = len(s) - 1
    flag = True
    while start <= end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            if flag and end - start == 1:
                ans.append(1)
                break
            elif flag and s[start + 1] == s[end] and s[start + 2] == s[end - 1]:
                start += 1
                flag = False
            elif flag and s[start] == s[end - 1] and s[start + 1] == s[end - 2]:
                end -= 1
                flag = False
            else:
                ans.append(2)
                break
    else:
        if flag:
            ans.append(0)
        else:
            ans.append(1)

for a in ans:
    print(a)
