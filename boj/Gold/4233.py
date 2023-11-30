import sys
input = sys.stdin.readline


def dqSqare(a, n, mod):
    if n == 1:
        return a
    elif n % 2 == 0:
        t = dqSqare(a, n // 2, mod)
        return (t * t) % mod
    else:
        return (a * dqSqare(a, n - 1, mod)) % mod


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    p, a = map(int, input().split())
    if p == a == 0:
        break

    print("yes" if not isPrime(p) and dqSqare(a, p, p) == a else "no")
