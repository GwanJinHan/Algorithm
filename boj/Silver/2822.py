scores = []

for i in range(8):
    n = int(input())
    scores.append((n, i + 1))

scores.sort(reverse=True)
acc = 0
ans = []

for i in range(5):
    acc += scores[i][0]
    ans.append(scores[i][1])

ans.sort()

print(acc)
print(*ans)
