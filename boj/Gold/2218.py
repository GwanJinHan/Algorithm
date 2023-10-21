import sys
input = sys.stdin.readline

n = int(input())
arr = []
ps = []
for i in range(n):
    num = int(input())
    arr.append(num)
    ps.append(num + ps[i - 1] if i != 0 else num)

end = 0
cur = 0
ans = -1
for start in range(n):

    while end < n and cur + arr[end] <= ps[start] + ps[-1] - ps[end]:
        cur += arr[end]
        end += 1

    ans = max(ans, cur)
    cur -= arr[start]

print(arr)
print(ps)
print(ans)

# 1 3 6 10 15
