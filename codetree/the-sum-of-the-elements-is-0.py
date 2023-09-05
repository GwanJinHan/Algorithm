import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

first_dic = {}
second_dic = {}

for i in range(n):
    for j in range(n):
        try:
            first_dic[a[i] + b[j]] += 1
        except:
            first_dic = 1

        try:
            second_dic[c[i] + d[j]] += 1
        except:
            second_dic = 1

cnt = 0
for k in first_dic.keys():
    if second_dic in -k:
        cnt += 1

print(cnt)
