t = int(input())
n = int(input())
arr_a = list(map(int, input().split()))
m = int(input())
arr_b = list(map(int, input().split()))

prefix_sum_a = [0]
prefix_sum_b = [0]

d_a = dict()
d_b = dict()

acc_a = 0
for i in range(n):
    acc_a += arr_a[i]
    for val in prefix_sum_a:
        try:
            d_a[acc_a - val] += 1
        except:
            d_a[acc_a - val] = 1
    prefix_sum_a.append(acc_a)

acc_b = 0
for i in range(m):
    acc_b += arr_b[i]
    for val in prefix_sum_b:
        try:
            d_b[acc_b - val] += 1
        except:
            d_b[acc_b - val] = 1
    prefix_sum_b.append(acc_b)

ans = 0
l = list(d_a.keys())
for key in l:
    try:
        ans += d_a[key] * d_b[t - key]
    except:
        continue

print(ans)
