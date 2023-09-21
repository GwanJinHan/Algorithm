import sys
input = sys.stdin.readline

n = int(input())

arr = [
    tuple(map(int, input().split())) for _ in range(n)
]

answer = []
for i in range(n):
    w, h = arr[i]
    cnt = 0
    for j in range(n):
        if w < arr[j][0] and h < arr[j][1]:
            cnt += 1

    answer.append(cnt + 1)

print(*answer)