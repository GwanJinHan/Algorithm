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
        cmd, key = input().rstrip().split()
        key = int(key)

        if cmd == "I":
            heapq.heappush(d, key)
            heapq.heappush(a, -key)
            try:
                dic[key] += 1
            except:
                dic[key] = 1
        elif cmd == "D":
            if len(s) == 0:
                continue
            elif key == -1 and dic[d[0]] != 0:
                t = heapq.heappop(d)
                dic[t] -= 1
            elif key == 1 and dic[-a[0]] != 0:
                t = heapq.heappop(a)
                dic[-t] -= 1
    if not any(dic.values()):
        print("EMPTY")
    else:
        min_val = heapq.heappop(d)
        max_val = -heapq.heappop(a)
        print(max_val, min_val)
