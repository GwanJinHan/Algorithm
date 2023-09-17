import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    t = input().rstrip()
    stack = []
    flag = False
    for val in t:
        if val == ")":
            if len(stack) == 0:
                flag = True
                break
            elif stack[-1] == "(":
                stack.pop()
            else:
                stack.append(val)
        else:
            stack.append(val)
    
    if flag or len(stack) != 0:
        print("NO")
    else:
        print("YES")
    