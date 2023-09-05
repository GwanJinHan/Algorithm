from collections import deque
import sys
import math
input = sys.stdin.readline
t = int(input())
s = [list(map(int, input().split())) for _ in range(t)]


def D(num):
    return (num * 2) % 10000


def S(num):
    return num - 1 if num != 0 else 9999


def L(num):
    l = int(math.log10(num))
    b, num = divmod(num, 10 ** l)
    return num * 10 + b


def R(num):
    l = int(math.log10(num))
    num, b = divmod(num, 10)
    return b * (10 ** l) + num


ans = []
for start, end in s:
    arr = [False] * 10000
    queue = [start]
    subqueue = []
    ans = []
    i = 0
    while queue:
        t = []
        subt = []
        for q in queue:
            arr[q - 1] = True

            prevsub = subqueue.pop() if len(subqueue) else ''
            if not arr[D(q) - 1]:
                t.append(D(q))
                subt.append(prevsub + "D")
            if not arr[S(q) - 1]:
                t.append(S(q))
                subt.append(prevsub + "S")
            if not arr[L(q) - 1]:
                t.append(L(q))
                subt.append(prevsub + "L")
            if not arr[R(q) - 1]:
                t.append(R(q))
                subt.append(prevsub + "R")


for val in ans:
    print(''.join(val))
