import sys
input = sys.stdin.readline

n = int(input())

matrix = [[0] * 52 for _ in range(52)]

for _ in range(n):
    a, _, b = input().rstrip().split()
    if a == b:
        continue
    matrix[ord(a) - 97 + 26 if a.islower() else ord(a) - 65][ord(b) -
                                                             97 + 26 if b.islower() else ord(b) - 65] = 1
for inter in range(52):
    for r in range(52):
        for c in range(52):
            if r == c or inter == c or inter == r:
                continue
            if matrix[r][inter] == 1 and matrix[inter][c] == 1:
                matrix[r][c] = 1

cnt = 0
ans = []
for i in range(52):
    for j in range(52):
        if matrix[i][j] != 0 and i != j:
            cnt += 1
            ans.append((i, j))

print(cnt)

for i, j in ans:
    print(chr(65 + i if i < 26 else i + 97 - 26),
          "=>", chr(65 + j if j < 26 else j + 97 - 26))
