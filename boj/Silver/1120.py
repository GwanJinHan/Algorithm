a, b = input().split()

min_diff = len(b)

for i in range(len(b) - len(a) + 1):
    diff = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            diff += 1
    min_diff = min(min_diff, diff)

print(min_diff)
