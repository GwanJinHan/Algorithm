import sys
input = sys.stdin.readline

n = int(input())

arr = [
    list(map(int, input().split())) for _ in range(n)
]

flag = False


for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c or r == inter or c == inter or arr[r][inter] == sys.maxsize or arr[inter][c] == sys.maxsize or arr[r][c] == sys.maxsize:
                continue
            elif arr[r][c] == arr[r][inter] + arr[inter][c]:
                arr[r][c] = sys.maxsize
                arr[c][r] = sys.maxsize
            elif arr[r][c] > arr[r][inter] + arr[inter][c]:
                flag = True
                break
        if flag:
            break
    if flag:
        break
if flag:
    print(-1)
else:
    acc = 0
    for val in arr:
        for v in val:
            if v != sys.maxsize:
                acc += v

    print(acc // 2)
