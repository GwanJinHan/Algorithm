import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    string = input().rstrip()
    s_set = set()
    s_set.add(string[0])
    flag = True
    for i in range(1, len(string)):
        if string[i] not in s_set:
            s_set.add(string[i])
        else:
            if string[i - 1] != string[i]:
                flag = False
                break

    if flag:
        ans += 1

print(ans)