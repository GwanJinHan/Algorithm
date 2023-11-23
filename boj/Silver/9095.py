import sys
input = sys.stdin.readline

t = int(input())

table = [1, 2, 4]

for _ in range(4, 11):
    table.append(table[-1] + table[-2] + table[-3])

for _ in range(t):
    num = int(input())
    print(table[num - 1])