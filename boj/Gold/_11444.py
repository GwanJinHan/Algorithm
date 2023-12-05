n = int(input())

a, b = 0, 1
for _ in range(50, 100):
    print(a)
    a, b = b, (a+b) % 1_000_000_007

print(b)
