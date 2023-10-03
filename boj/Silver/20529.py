import sys
input = sys.stdin.readline

t = int(input())

answers = []


def compareStrings(arr):
    cnt = 0
    for i in range(2):
        for j in range(i + 1, 3):
            for k in range(4):
                if arr[i][k] != arr[j][k]:
                    cnt += 1
    return cnt


for _ in range(t):
    n = int(input())
    arr = list(input().rstrip().split())

    ans = sys.maxsize
    for i in range(1, n - 1):
        ans = min(ans, compareStrings([arr[i], arr[i - 1], arr[i + 1]]))

    answers.append(ans)

for a in answers:
    print(a)
