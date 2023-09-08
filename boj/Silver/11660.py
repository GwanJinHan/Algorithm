import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}

for r in range(1, n + 1):
    total = 0
    t = list(map(int, input().split()))

    for c in range(1, n + 1):
        total += t[c - 1]
        d[f'{r}{c}'] = total

ans = []

for _ in range(m):
    answer = 0
    r1, c1, r2, c2 = list(map(int, input().split()))

    for i in range(r1, r2 + 1):
        answer += d[f'{i}{c2}'] - d[f'{i}{c1 - 1}'] if c1 - \
            1 != 0 else d[f'{i}{c2}']

    ans.append(answer)

for val in ans:
    print(val)
