def precedence(op):
    if op == "(" or op == ")":
        return 0
    elif op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2


o = input()
stack = []
ans = []
for s in o:
    if s == "(":
        stack.append("(")
    elif s == ")":
        while stack:
            op = stack.pop()
            if op == "(":
                break
            else:
                ans.append(op)
    elif s in "+*/-":
        while stack:
            op = stack[-1]
            if precedence(op) >= precedence(s):
                ans.append(stack.pop())
            else:
                break
        stack.append(s)

    else:
        ans.append(s)

while stack:
    ans.append(stack.pop())

print(''.join(ans))
