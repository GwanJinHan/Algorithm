string = input()


def srt(x):
    if x in '*/':
        return 2
    elif x in '+-':
        return 3
    else:
        return 1


# 괄호처리
t_stack = []
for s in string:
    if s == ')':
        t = ''
        while t_stack[-1] != '(':
            t = t_stack.pop() + t
        else:
            t_stack.pop()
        t_stack.append(''.join(sorted(t, key=srt)))
    else:
        t_stack.append(s)

stack = []
ans = []

# # */ 처리
isModDiv = False
for s in t_stack:
    if isModDiv:
        stack.append(s)
        ans.extend(sorted(stack, key=srt))
        stack.clear()
        isModDiv = False
    elif s in '*/':
        isModDiv = True
        stack.append(s)
    else:
        stack.append(s)

ans = sorted([''.join(ans), *stack], key=srt)

print(''.join(ans))
