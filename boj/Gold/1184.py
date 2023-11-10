import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

leftuprightdown = [[0] * (n + 1) for _ in range(n + 1)]
rightupleftdown = [[0] * (n + 1) for _ in range(n + 1)]
rightdownleftup = [[0] * (n + 1) for _ in range(n + 1)]
leftdownrightup = [[0] * (n + 1) for _ in range(n + 1)]


for r in range(1, n + 1):
    for c in range(1, n + 1):
        leftuprightdown[r][c] = arr[r - 1][c - 1] + \
            leftuprightdown[r - 1][c] + leftuprightdown[r][c -
                                                           1] - leftuprightdown[r - 1][c - 1]

for r in range(n - 1, -1, -1):
    for c in range(1, n + 1):
        leftdownrightup[r][c] = arr[r][c - 1] + \
            leftdownrightup[r + 1][c] + leftdownrightup[r][c -
                                                           1] - leftdownrightup[r + 1][c - 1]

for r in range(1, n + 1):
    for c in range(n - 1, -1, -1):
        rightupleftdown[r][c] = arr[r - 1][c] \
            + rightupleftdown[r - 1][c] + rightupleftdown[r][c +
                                                             1] - rightupleftdown[r - 1][c + 1]

for r in range(n - 1, -1, -1):
    for c in range(n - 1, -1, -1):
        rightdownleftup[r][c] = arr[r][c] \
            + rightdownleftup[r + 1][c] + rightdownleftup[r][c +
                                                             1] - rightdownleftup[r + 1][c + 1]


cnt = 0
for i in range(1, n):
    for j in range(1, n):
        d = {}
        for r in range(i):
            for c in range(j):

                t = leftuprightdown[i][j] - leftuprightdown[r][j] - \
                    leftuprightdown[i][c] + leftuprightdown[r][c]

                try:
                    d[t] += 1
                except:
                    d[t] = 1

        for r in range(i + 1, n + 1):
            for c in range(j + 1, n + 1):

                t = rightdownleftup[i][j] - rightdownleftup[r][j] - \
                    rightdownleftup[i][c] + rightdownleftup[r][c]

                try:
                    cnt += d[t]
                except:
                    pass


for i in range(1, n):
    for j in range(1, n):
        d = {}
        for r in range(i):
            for c in range(j + 1, n + 1):

                t = rightupleftdown[i][j] - rightupleftdown[r][j] - \
                    rightupleftdown[i][c] + rightupleftdown[r][c]

                try:
                    d[t] += 1
                except:
                    d[t] = 1

        for r in range(i + 1, n + 1):
            for c in range(j):

                t = leftdownrightup[i][j] - leftdownrightup[r][j] - \
                    leftdownrightup[i][c] + leftdownrightup[r][c]

                try:
                    cnt += d[t]
                except:
                    pass

print(cnt)
