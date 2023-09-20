from collections import deque
n, k = map(int, input().split())
d = deque(range(1, n + 1))

answer = []
i = 1
while d:
    cur = d.popleft()
    if i % k == 0:
        answer.append(cur)
    else:
        d.append(cur)
    i += 1
answer = map(str, answer)
print("<" + ', '.join(answer) + ">")
