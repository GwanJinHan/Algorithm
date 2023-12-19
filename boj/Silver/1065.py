n = int(input())
cnt = 0
for num in range(1, n + 1):
    s = str(num)
    flag = False
    for i in range(len(s) - 2):
        if int(s[i + 1]) - int(s[i]) != int(s[i + 2]) - int(s[i + 1]):
            flag = True
            break
    if not flag:
        cnt += 1


print(cnt)
