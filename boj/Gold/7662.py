import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    d = []
    s = set()
    for _ in range(1, n + 1):
        cmd, key = input().rstrip().split()
        key = int(key)

        if cmd == "I":
            heapq.heappush(d, key)
            heapq.heappush(a, -key)
            s.add(key)
        elif cmd == "D":
            if len(s) == 0:
                continue
            elif key == -1 and d[0] in s:
                t = heapq.heappop(d)
                s.remove(t)
            elif key == 1 and -a[0] in s:
                t = heapq.heappop(a)
                s.remove(-t)
    if len(s) == 0:
        print("EMPTY")
    else:
        min_val = heapq.heappop(d)
        max_val = -heapq.heappop(a)
        print(max_val, min_val)
