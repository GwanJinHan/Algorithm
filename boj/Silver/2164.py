from collections import deque
n = int(input())
d = deque(range(1, n + 1))

i = 0
while len(d) != 1:
    if i % 2 == 0:
        d.popleft()
    else:
        d.append(d.popleft())
    i += 1

print(*d)