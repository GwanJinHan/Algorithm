import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
d = {}

for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

arr.sort()

# 포인터 두 개
# 만약 k보다 커지면 break
# 무게 더한 값을 딕셔너리로 관리. (try, except)

for i in range(n):
    for j in range(i, n):
        if arr[i][0] + arr[j][0] > k:
            break

        if i == j:
            try:
                d[arr[i][0]] = max(d[arr[i][0]], arr[i][1])
            except:
                d[arr[i][0]] = arr[i][1]
        else:
            try:
                d[arr[i][0] + arr[j][0]
                  ] = max(d[arr[i][0] + arr[j][0]], arr[i][1] + arr[j][1])
            except:
                d[arr[i][0] + arr[j][0]] = arr[i][1] + arr[j][1]

print(max(d.values()))
