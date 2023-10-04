from collections import deque
import sys
input = sys.stdin.readline
t = int(input())


def D(num):
    return (num * 2) % 10000


def S(num):
    return num - 1 if num != 0 else 9999


def L(num):
    d4 = num % 10
    num //= 10
    d3 = num % 10
    num //= 10
    d2 = num % 10
    num //= 10
    d1 = num

    return (d2 * 1000 + d3 * 100 + d4 * 10 + d1)


def R(num):
    d4 = num % 10
    num //= 10
    d3 = num % 10
    num //= 10
    d2 = num % 10
    num //= 10
    d1 = num

    return (d4 * 1000 + d1 * 100 + d2 * 10 + d3)


for _ in range(t):
    a, b = map(int, input().split())
    queue = deque([a])
    visited = [False] * 10000
    visited[a] = ""

    while queue:
        cur_n = queue.popleft()

        d, s, l, r = D(cur_n), S(cur_n), L(cur_n), R(cur_n)

        if not visited[d]:
            if d == b:
                print(visited[cur_n] + "D")
                break
            queue.append(d)
            visited[d] = visited[cur_n] + "D"

        if not visited[s]:
            if s == b:
                print(visited[cur_n] + "S")
                break
            queue.append(s)
            visited[s] = visited[cur_n] + "S"

        if not visited[l]:
            if l == b:
                print(visited[cur_n] + "L")
                break
            queue.append(l)
            visited[l] = visited[cur_n] + "L"

        if not visited[r]:
            if r == b:
                print(visited[cur_n] + "R")
                break
            queue.append(r)
            visited[r] = visited[cur_n] + "R"
