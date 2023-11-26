import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

MAX = 0
MIN = 500
d = {}
for _ in range(n):
    t = list(map(int, input().split()))
    for val in t:
        MAX = max(MAX, val)
        MIN = min(MIN, val)
        try:
            d[val] += 1
        except:
            d[val] = 1

ans = sys.maxsize
ans_h = 500

d_items = list(d.items())


for h in range(MIN, MAX + 1):
    t_time = 0
    t_b = b
    flag = False

    for key, val in d_items:
        if key > h:
            t_time += (key - h) * 2 * val
            t_b += (key - h) * val
        elif key < h:
            t_time += (h - key) * val
            t_b -= (h - key) * val


    if t_b >= 0 and ans >= t_time:
        ans = t_time
        ans_h = h

print(ans, ans_h)
