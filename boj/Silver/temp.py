n = int(input())

i = 0
while True:
    if n == 1:
        print(1)
        break
    i += 1
    if 3 * (i ** 2) - 3 * i + 2 <= n <= 3 * (i ** 2) + 3 * i + 1:
        print(i + 1)
        break