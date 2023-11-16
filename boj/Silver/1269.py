n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

u = len(a & b)
print(n + m - u - u)
