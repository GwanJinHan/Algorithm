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
            heapq.heappush(a, key)
            heapq.heappush(d, -key)
            try:
                dic[key] += 1
            except:
                dic[key] = 1
        elif cmd == "D":
            if len(dic) == 0:
                continue
            elif key == -1:
                try:
                    t = heapq.heappop(a)
                    while t not in dic:
                        t = heapq.heappop(a)
                    dic[t] -= 1
                    if dic[t] == 0:
                        dic.pop(t)
                except:
                    continue
            elif key == 1:
                try:
                    t = heapq.heappop(d)
                    while -t not in dic:
                        t = heapq.heappop(d)
                    dic[-t] -= 1
                    if dic[-t] == 0:
                        dic.pop(-t)
                except:
                    continue
    if sum(dic.values()) <= 0:
        print("EMPTY")
    else:
        max_val = -sys.maxsize
        min_val = sys.maxsize
        for key, value in dic.items():
            if value != 0:
                max_val = max(max_val, key)
                min_val = min(min_val, key)

        print(max_val, min_val)
