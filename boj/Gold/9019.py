from collections import deque
import sys
input = sys.stdin.readline
t = int(input())


def D(num):
    return (num * 2) % 10000


def S(num):
    return num - 1 if num != 0 else 9999


def L(num):
    a, b = divmod(num, 1000)
    return b * 10 + a


def R(num):
    a, b = divmod(num, 10)
    return b * 1000 + a


for _ in range(t):
    a, b = map(int, input().split())
    queue = deque([(a, "")])
    visited = [False] * 10000
    visited[a] = True

    while queue:
        cur_n, cmds = queue.popleft()

        if cur_n == b:
            print(cmds)
            break

        d, s, l, r = D(cur_n), S(cur_n), L(cur_n), R(cur_n)
        if not visited[d]:
            queue.append((d, cmds + "D"))
            visited[d] = True
        if not visited[s]:
            queue.append((s, cmds + "S"))
            visited[s] = True
        if not visited[l]:
            queue.append((l, cmds + "L"))
            visited[l] = True
        if not visited[r]:
            queue.append((r, cmds + "R"))
            visited[r] = True
