import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
nums = list(range(n, 0, -1))

for _ in range(n):
    num = int(input())

    while not stack or stack[-1] != num:
        try:
            stack.append(nums.pop())
            ans.append("+")
        except:
            print("NO")
            sys.exit(0)

    stack.pop()
    ans.append("-")

for a in ans:
    print(a)
