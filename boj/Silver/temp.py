a, b, v = map(int, input().split())

t = (v - a - b) // (a - b) + 2 if (v - a -
                                   b) % (a - b) <= a else (v - a - b) // (a - b) + 2
print(t)
