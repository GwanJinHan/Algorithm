import sys
from collections import deque
input = sys.stdin.readline

n, g = map(int, input().split())

queue = deque([1])
route = set([1])
sets = [set(list(map(int, input().split()))[1:]) for _ in range(g)]

cnt = 0
while queue:
    q = queue.popleft()
    for s in sets:
        try:
            s.remove(q)
        except:
            pass
        if len(s) == 1 and list(s)[0] not in route:
            queue.append(*s)
            route.add(*s)
    cnt += 1

print(cnt)
