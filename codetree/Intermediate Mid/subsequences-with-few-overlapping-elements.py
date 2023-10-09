from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = end = 0
ans = -1
d = {}
while end < n and start <= end:
    # 만약 end 원소의 개수가 k개 초과라면
    # start = 초과하는 원소의 가장 왼쪽 요소 + 1
    # popleft
    if arr[end] in d and len(d[arr[end]]) >= k:
        start = d[arr[end]].popleft() + 1

    # end 원소의 개수가 k개 이하라면
    # end += 1
    else:
        try:
            d[arr[end]].append(end)
        except:
            d[arr[end]] = deque([end])

    end += 1
    ans = max(ans, end - start)

print(ans)
