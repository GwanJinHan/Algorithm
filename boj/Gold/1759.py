from itertools import combinations as cb

l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
cmbs = list(cb(arr, l))
vowels = set(['a', 'e', 'i', 'o', 'u'])
for t in cmbs:
    v = 0
    for s in t:
        if s in vowels:
            v += 1

    if v >= 1 and l - v >= 2:
        print(''.join(t))
