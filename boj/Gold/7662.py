import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    d = []
    dic = dict()
    for _ in range(1, n + 1):
        cmd, key = input().split()
        key = int(key)

        if cmd == "I":
            heapq.heappush(d, key)
            heapq.heappush(a, -key)
            try:
                dic[key] += 1
            except:
                dic[key] = 1
        elif cmd == "D":
            if len(d) == 0:
                continue
            elif key == -1:
                try:
                    t = heapq.heappop(a)
                    dic[t] -= 1
                except:
                    continue
            elif key == 1:
                try:
                    t = heapq.heappop(d)
                    dic[-t] -= 1
                except:
                    continue
    if sum(dic.values()) <= 0:
        print("EMPTY")
    else:
        min_val = heapq.heappop(a)
        max_val = -heapq.heappop(d)
        print(max_val, min_val)
