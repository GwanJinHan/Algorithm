import sys
from collections import deque
input = sys.stdin.readline

n = int(input())


def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


for _ in range(n):
    s, e = input().rstrip().split()
    visited = set()
    q = deque([(list(s), 0)])

    while q:
        x, w = q.popleft()

        l = int(''.join(x))

        if l in visited:
            continue
        visited.add(l)

        if l == e:
            print(w)
            break

        for i in range(4):
            for j in range(1, 10):
                t = str((int(x[i]) + j) % 10)

                if i == 0 and t == '0':
                    continue

                u = x.copy()
                u[i] = t
                k = int(''.join(u))

                if k not in visited and isPrime(k):
                    q.append((u, w + 1))
