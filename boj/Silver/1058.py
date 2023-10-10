import sys
input = sys.stdin.readline

n = int(input())

arr = [
    list(input().rstrip()) for _ in range(n)
]

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c or inter == r or inter == c:
                continue
            elif arr[r][c] == 'Y':
                continue

            elif arr[r][inter] == "Y" and arr[inter][c] == "Y":
                arr[r][c] = "y"

ans = -1

for val in arr:
    ans = max(ans, val.count("Y") + val.count("y"))

print(ans)
