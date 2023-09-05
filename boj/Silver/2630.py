import sys
input = sys.stdin.readline
n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]


def is_valid(arr, f):
    for val in arr:
        if val != f:
            return False
    return True


def devide(r, c, length):
    f = arr[r][c]
    for i in range(r, r + length):
        if not is_valid(arr[i][c: c + length], f):
            ans = [0, 0]
            for w, b in [devide(r, c, length // 2),
                         devide(r + length // 2, c, length // 2),
                         devide(r, c + length // 2, length // 2),
                         devide(r + length // 2,
                                c + length // 2, length // 2)]:
                ans[0] += w
                ans[1] += b

            return ans
    if arr[r][c]:
        return [0, 1]
    else:
        return [1, 0]


w, b = devide(0, 0, n)

print(w)
print(b)
