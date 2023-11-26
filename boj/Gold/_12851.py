from collections import deque

n, k = map(int, input().split())

visit = [False] * 100001
secs = [0] * 100001
queue = deque([n])

ans = 100002
while queue:
    pos, sec = queue.popleft()

    if visit[pos] and sec > :
        continue
    
    if pos == k:
        if ans > sec:
            ans = sec
            cnt = 1
        elif ans == sec:
            cnt += 1
        continue
    else:
        visit[pos] = True

    if 0 <= pos - 1 < 100001:
        queue.append((pos - 1, sec + 1))
    
    if 0 <= pos + 1 < 100001:
        queue.append((pos + 1, sec + 1))
        
    if 0 <= pos * 2 < 100001:
        queue.append((pos * 2, sec + 1))
        

print(ans)
print(cnt)