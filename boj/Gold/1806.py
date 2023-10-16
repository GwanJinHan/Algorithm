n, s = map(int, input().split())
arr = list(map(int, input().split()))

start = end = 0
min_length = n + 1
current_sum = 0

while end < n:
    current_sum += arr[end]
    end += 1

    while current_sum >= s:
        min_length = min(min_length, end - start)
        current_sum -= arr[start]
        start += 1

if min_length == n + 1:
    print(0)
else:
    print(min_length)
