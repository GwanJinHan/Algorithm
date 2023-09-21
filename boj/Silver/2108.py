import sys
input = sys.stdin.readline

n = int(input())

acc = 0
d = {}
arr = []

for _ in range(n):
    num = int(input())
    acc += num
    arr.append(num)
    try:
        d[num] += 1
    except:
        d[num] = 1
arr.sort()
# 산술평균, 중앙값, 최빈값, 범위

print(round(acc / n))
print(arr[(n + 1) // 2 - 1])

mode = list(d.items())
mode.sort(key = lambda x : (-x[1], x[0]))

if len(mode) == 1:
    print(arr[0])
elif mode[0][1] == mode[1][1]:
    print(mode[1][0])
else:
    print(mode[0][0])

print(max(arr) - min(arr))