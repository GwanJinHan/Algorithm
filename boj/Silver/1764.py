import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = set()
b = set()

for _ in range(n):
    d.add(input().rstrip())
for _ in range(m):
    b.add(input().rstrip())

dbj = sorted(d & b)

print(len(dbj))
for val in dbj:
    print(val)
