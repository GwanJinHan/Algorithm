import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
nums = list(range(n, 0, -1))
flag = False
for _ in range(n - 1):
    num = int(input())

    while not stack or stack[-1] != num:
        if not stack:
            stack.append(nums.pop())
        elif stack[-1] > num:
            if not stack:
                print("NO")
                sys.exit(0)
            stack.pop()
            ans.append("-")
            if stack[-1] == num:
                ans.append("-")
                stack.pop()
        elif stack[-1] < num:
            try:
                stack.append(nums.pop())
                ans.append("+")
            except:
                print("NO")
                sys.exit(0)
print(ans)
