import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []

for _ in range(n):
    num = int(input())

    if not stack or num > stack[-1]:
        stack.extend(range(1, num))
        ans.extend(["+"] * (num))
    else:
        stack.pop()
        ans.append('-')
