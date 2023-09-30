a, b, v = map(int, input().split())

t = (v - a) // (a - b) + 1
print(t + 1)
