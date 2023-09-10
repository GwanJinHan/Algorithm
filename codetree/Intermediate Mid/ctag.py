# A와 B간 교집합을 공집합으로
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [
    input().rstrip() for _ in range(n)
]
b = [
    input().rstrip() for _ in range(n)
]

cnt = 0

for i in range(m - 2):
    for j in range(i + 1, m - 1):
        for k in range(j + 1, m):
            a_strings = set([
                v[i] + v[j] + v[k] for v in a
            ])
            b_strings = set([
                v[i] + v[j] + v[k] for v in b
            ])

            if not (a_strings & b_strings):
                cnt += 1

print(cnt)
