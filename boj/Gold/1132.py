import sys
input = sys.stdin.readline

n = int(input())

d = {}
start = set()

for _ in range(n):
  string = input().rstrip()
  start.add(string[0])

  for i, s in enumerate(string):
    try:
      d[s] += 10 ** (len(string) - i - 1)
    except:
      d[s] = 10 ** (len(string) - i - 1)

#start에 없는 수 중 val 이 가장 작은 수가 0이 됨 (만약 a~j까지 모두 나왔을 때)
vs = list(d.items())
vs.sort(key = lambda x: -x[1])
if len(d) == 10:
  for i in range(9, -1, -1):
    if vs[i][0] not in start:
      del vs[i]
      break

ans = 0
num = 9
for alph, val in vs:
  ans += num * val
  num -= 1

print(ans)
