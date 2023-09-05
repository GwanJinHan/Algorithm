n, r, c = map(int, input().split())

# 2^n X 2^n 크기의 정방행렬
# 초기는 [0]
# 정사각형을 4등분한다. 왼쪽 위는 그대로, 오른쪽 위는 모두 4^(n-1) X 1 를 더한다. 왼쪽 아래는 모두 4^(n-1) X 2 더하고, 오른쪽 아래는 4^(n-1) X 3
# 2^(n-1) * 2^(n-1) => 이전 사각형의 넓이

arr = [[0]]

for i in range(1, n + 1):
    temp = arr.copy()
    temp += [[] for _ in range(2 ** (i - 1))]

    # 오른쪽 위
    for row in range(2 ** (i - 1)):
        for col in range(2 ** (i - 1)):
            temp[row].append(arr[row][col] + 4**(i - 1)*1)
            temp[row + 2**(i - 1)].append(arr[row][col] + 4**(i - 1)*2)

    for row in range(2 ** (i - 1)):
        for col in range(2 ** (i - 1)):
            temp[row + 2**(i - 1)].append(arr[row][col] + 4**(i - 1)*3)

    arr = temp.copy()

print(arr[r][c])
