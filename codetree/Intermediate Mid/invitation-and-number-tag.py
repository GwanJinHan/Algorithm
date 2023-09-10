import sys
input = sys.stdin.readline

n, g = map(int, input().split())

sets = []

queue = set([1])
sets = [set(list(map(int, input().split()))[1:]) for _ in range(g)]

cnt = 0
while queue:
    t = set()
    for s in sets:
        for q in queue:
            try:
                s.remove(q)
            except:
                pass
        if len(s) == 1:
            t.add(*s)
    cnt += len(queue)
    queue = t

print(cnt)
