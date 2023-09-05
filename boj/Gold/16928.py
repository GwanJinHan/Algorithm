import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ladders = {k: v for _ in range(n) for k, v in [map(int, input().split())]}
snakes = {k: v for _ in range(m) for k, v in [map(int, input().split())]}

queue = [1]
arrived = False
cnt = 0
while queue and not arrived:
    cnt += 1
    t = []
    for q in queue:
        for i in range(q + 1, q + 7):
            if i == 100:
                arrived = True
                break
            if i in ladders.keys() and ladders[i] not in t:
                t.append(ladders[i])
            elif i in snakes.keys() and snakes[i] not in t:
                t.append(snakes[i])
            else:
                if i not in t:
                    t.append(i)

        if arrived:
            break

    queue = t.copy()


print(cnt)
