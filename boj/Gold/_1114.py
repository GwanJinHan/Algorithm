# 변하는 것 : 가장 긴 조각 => 이분탐색 (시작 : 0 , l)
# l : 통나무 길이 / k : 자를 수 있는 위치 개수 / c : 자를 수 있는 횟수

l, k, c = map(int, input().split())
arr = list(map(int, input().split())) + [l]  # 자를 수 있는 위치들

left = 0
right = l

while left <= right:
    mid = (left + right) // 2

    start = 0
    tmp = 0
    cnt = 0
    for t in arr:
        if t - start > mid:
            start = tmp
            cnt += 1
        elif t - start == mid:
            start = t
            cnt += 1

        if cnt > c:
            left = mid + 1
            break

        tmp = t

    if cnt < c:
        right = mid - 1

    if cnt == c:
        break

for i in range(k):
    if arr[i] > mid:
        print(mid, arr[i - 1])
        break
    if arr[i] == mid:
        print(mid, arr[i])
        break
