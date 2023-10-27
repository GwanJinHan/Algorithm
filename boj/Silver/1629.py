a, b, c = map(int, input().split())


def dq(C, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        t = dq(C, n // 2)
        return t * t % c
    else:
        t = dq(C, n // 2)
        return C * t * t % c


print(dq(a, b))
