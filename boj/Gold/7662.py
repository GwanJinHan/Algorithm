n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

d = {}

for val in a:
    try:
        d[val] += 1
    except:
        d[val] = 1

for tar in b:
    try:
        print(d[tar], end=" ")
    except:
        print(0, end=" ")
