import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque()

for _ in range(n):
  cmd,*num = input().rstrip().split()
  if num: num = int(num[0])

  if cmd == "push":
    queue.append(num)
  elif cmd == "pop":
    try:
      print(queue.popleft())
    except:
      print(-1)
  elif cmd == "size":
    print(len(queue))
  elif cmd == "empty":
    print(1 if len(queue) == 0 else 0)
  elif cmd == "front":
    try:
      print(queue[0])
    except:
      print(-1)
  elif cmd == "back":
    try:
      print(queue[-1])
    except:
      print(-1)