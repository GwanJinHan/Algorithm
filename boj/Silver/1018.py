import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [
  list(input()) for _ in range(n)
]

ans = sys.maxsize
for r in range(n - 7):
  for c in range(m - 7):
    b_first = 0
    w_first = 0
    for y in range(r, r + 8):
      for x in range(c, c + 8):
        val = arr[y][x]
        if y % 2 == 0 and x % 2 == 0:
          if val == "W":
            b_first += 1
          else:
            w_first += 1
        elif y % 2 != 0 and x % 2 == 0:
          if val == "B":
            b_first += 1
          else:
            w_first += 1
        elif y % 2 == 0 and x % 2 != 0:
          if val == "B":
            b_first += 1
          else:
            w_first += 1
        elif y % 2 != 0 and x % 2 != 0:
          if val == "W":
            b_first += 1
          else:
            w_first += 1
    ans = min([ans, b_first, w_first])

print(ans)
