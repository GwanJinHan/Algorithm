import sys
input = sys.stdin.readline

n = int(input())
matrix = [[0] * 26 for _ in range(26)]

for _ in range(n):
    a, _, b = input().rstrip().split()
    matrix[ord(a) - 97][ord(b) - 97] = 1

for inter in range(26):
    for r in range(26):
        for c in range(26):
            if r == c or r == inter or c == inter:
                continue

            if matrix[r][inter] == 1 and matrix[inter][c] == 1:
                matrix[r][c] = 1

m = int(input())
for _ in range(m):
    a, _, b = input().rstrip().split()
    if matrix[ord(a) - 97][ord(b) - 97] == 1:
        print("T")
    else:
        print("F")
