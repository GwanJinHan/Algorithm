import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 경로가 없는 경우 무한으로 설정
arr = [[sys.maxsize] * n for _ in range(n)]

# 버스 노선 비용 갱신 (2차원 배열)
for _ in range(m):
    a, b, cost = map(int, input().split())

    # 노선이 여러 개인 경우 더 비용이 작은 것으로
    arr[a - 1][b - 1] = min(cost, arr[a - 1][b - 1])

# 자기 자신은 0으로 설정
for i in range(n):
    arr[i][i] = 0

for inter in range(n):
    for r in range(n):
        for c in range(n):
            # 거쳐가는 노드가 출발노드나 도착노드에 해당하는 경우 continue
            if inter == r or inter == c:
                continue

            arr[r][c] = min(arr[r][c], arr[r][inter] + arr[inter][c])

for r in range(n):
    for c in range(n):
        if arr[r][c] == sys.maxsize:
            arr[r][c] = 0

for val in arr:
    print(*val)
