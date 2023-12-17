from collections import deque as dq
import itertools

n, k = map(int, input().split())
stack = dq()
arr = list(map(int, list(input())))
cnt = k
for val in arr:
    if len(stack) == 0:
        stack.append(val)
    elif stack[-1] < val and cnt > 0:
        while stack and stack[-1] < val and cnt > 0:
            stack.pop()
            cnt -= 1
        stack.append(val)
    else:
        stack.append(val)

print(''.join(map(str, list(itertools.islice(stack, 0, n - k)))))
