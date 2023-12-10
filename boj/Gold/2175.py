arr = list(map(int, input().split()))

dots = []

for i in range(4):
    x1, y1 = arr[i * 2], arr[i * 2 + 1]
    x2, y2 = arr[(i + 1) * 2 % 8], arr[((i + 1) * 2) % 8 + 1]
    dots.append((x1, y1))
    dots.append(((x1 + x2) / 2, (y1 + y2) / 2))


def getArea(arr):
    acc = 0
    for i in range(len(arr)):
        acc += (arr[i][0] + arr[(i + 1) % len(arr)][0]) * \
            (arr[i][1] - arr[(i + 1) % len(arr)][1])
    return abs(acc) / 2


total = getArea(dots)
diff = total
ans = total
for i in range(7):
    for j in range(i + 1, 8):
        t = getArea(dots[i:j + 1])
        if diff > abs(t - (total - t)):
            diff = abs(t - (total - t))
            ans = t

print(min(ans, total - ans), max(ans, total - ans))
