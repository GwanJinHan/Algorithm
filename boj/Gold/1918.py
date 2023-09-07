string = input()

stack_nums = []
stack_oper = []
ans = ''


def srt(x):
    if x in '*/':
        return 2
    elif x in '+-':
        return 1
    else:
        return 3


# */ 처리
isMulDiv = False
for s in string:
    if isMulDiv:
        stack_nums[-1] = stack_nums[-1] + s + stack_oper.pop()
        isMulDiv = False
    elif s == '*' or s == '/':
        stack_oper.append(s)
        isMulDiv = True
    elif s.isalpha:
        stack_nums.append(s)
    elif s == '+' or s == '-':
        stack_oper.append(s)
    else:
        stack_nums.append(s)
print(stack_nums)
# 괄호처리
t_stack = []
for s in stack_nums:
    if s == ')':
        t = ''
        while t_stack[-1] != '(':
            t = t_stack.pop() + t
        else:
            t_stack.pop()
        t_stack.append(t.sort(key=srt))
    else:
        t_stack.append(s)
# +- 처리
ans = []
isOper = ''
for s in t_stack:
    if isOper:
        ans[-1] = ans[-1] + s + isOper
        isOper = ''
    elif s in '+-':
        isOper = s
    else:
        ans.append(s)
print(*ans)
