from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = []
visited = [[True] * n for _ in range(n)]
queue = deque()

for i in range(n):
    t = list(map(int, input().split()))
    if 9 in t:
        queue.append((i, t.index(9), 2))
    arr.append(t)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

while queue:
    r, c, sec = queue.popleft()

    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]

        if 0 <= nr < n and 0 <= nc < n:
            

