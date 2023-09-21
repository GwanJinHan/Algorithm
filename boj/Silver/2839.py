import sys

n = int(input())

max_5 = n // 5
left = n % 5

while left % 3 != 0:
    if max_5 == 0 and left != 0:
        print(-1)
        sys.exit()
        break
    max_5 -= 1
    left += 5

print(max_5 + left // 3)