import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
queue = deque()
for i in range(n):
    t = input().rstrip()
    if "I" in t:
        queue.append((t.index("I"),i))
    
    arr.append(list(t))

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and 