import sys
input = sys.stdin.readline

n = int(input())

arr = []
d = {}
for i in range(n):
  age, name = input().rstrip().split()
  age = int(age)
  arr.append([age, name, i])

arr.sort(key=lambda x: (x[0], x[2]))

for val in arr:
  print(*val[:2])