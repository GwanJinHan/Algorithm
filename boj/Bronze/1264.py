import sys
input = sys.stdin.readline

v = "aeiouAEIOU"

while True:
    s = input().rstrip()

    if s == "#":
        break
    cnt = 0
    for i in s:
        if i in v:
            cnt += 1

    print(cnt)
