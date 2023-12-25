N, M = map(int, input().split())
pattern = [input() for _ in range(N)]

for row in pattern:
    print(row[::-1])
