import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
  cmd,*num = input().rstrip().split()
  if num: num = int(num[0])

  if cmd == "push":
    stack.append(num)
  elif cmd == "pop":
    try:
      print(stack.pop())
    except:
      print(-1)
  elif cmd == "size":
    print(len(stack))
  elif cmd == "empty":
    print(1 if len(stack) == 0 else 0)
  elif cmd == "top":
    try:
      print(stack[-1])
    except:
      print(-1)