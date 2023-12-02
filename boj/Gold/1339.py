n = int(input())
d_alph = {}

for _ in range(n):
    string = input()
    l = len(string)
    for i,  s in enumerate(string):
        try:
            d_alph[s] += 10 ** (l - i - 1)
        except:
            d_alph[s] = 10 ** (l - i - 1)

d_values = list(d_alph.values())
d_values.sort(reverse=True)

k = 9
ans = 0
for v in d_values:
    ans += v * k
    k -= 1

print(ans)
