from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ladders = {}
snakes = {}

for _ in range(n):
    s, e = map(int, input().split())
    ladders[s] = e

for _ in range(m):
    s, e = map(int, input().split())
    snakes[s] = e

visited = [False] * 100
queue = deque([(1, 0)])

while queue:
    cur_lo, cur_cnt = queue.popleft()

    if visited[cur_lo]:
        continue

    visited[cur_lo] = True

    for lo in range(cur_lo + 1, cur_lo + 7):
        if lo == 100:
            queue.clear()
            print(cur_cnt + 1)
            break
        if visited[lo]:
            continue
        if lo in ladders:
            if not visited[ladders[lo]]:
                queue.append((ladders[lo], cur_cnt + 1))

        elif lo in snakes:
            if not visited[snakes[lo]]:
                queue.append((snakes[lo], cur_cnt + 1))

        elif not visited[lo]:
            queue.append((lo, cur_cnt + 1))
