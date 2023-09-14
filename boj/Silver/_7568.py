import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = []

for val in arr:
    cnt = 0
    for tar in arr:
        if val[0] > tar[0] and val[1] > tar[1]:
            cnt += 1
    ans.append(cnt + 1)

print(*ans)