n = int(input())
arr = list(map(int, input().split()))

firstList = [0]
secondList = [arr[0]]

for i, val in enumerate(arr):
    if i == 0:
        continue
    if val > arr[i - 1]:
        for k, s in enumerate(secondList):
            if s > val:
                key = k - 1
                secondList[key] = val
                break
        else:
            secondList.append(val)
    else:
        for j, a in enumerate(secondList):
            if val <= a:
                secondList[j] = val
                firstList.append(j)
                break
# val:2,
print(firstList)
print(secondList)
