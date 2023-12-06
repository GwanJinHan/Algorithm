import sys


n = int(input())
arr = []


def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if n < 8:
    print(-1)
    sys.exit(0)

if n % 2 == 1:
    n -= 5
    print("2 3 ", end="")
else:
    n -= 4
    print("2 2 ", end="")

for i in range(2, n + 1):
    if isPrime(i) and isPrime(n - i):
        print(i, n - i)
        break
