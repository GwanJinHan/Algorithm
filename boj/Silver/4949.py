import sys
input = sys.stdin.readline
ans = []
open = ["(", "["]
close = [")", "]"]

while True:
    string = input().rstrip()
    if string == ".":
        break

    stack = []

    for s in string:
        if s in open:
            stack.append(s)
        elif s in close:
            if s == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif s == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        if not stack:
            print("yes")
        else:
            print("no")
