from collections import deque

n = int(input())
m = int(input())
string = list(input())

I_flag = False  # 현재 문자가 I임을 기록
queue = deque()
cnt = 0
target = 2 * n + 1

for i, s in enumerate(string):
    if s == "I":
        if I_flag == True:  # II
            queue.clear()
            queue.append(i)
        else:  # OI
            I_flag = True
            queue.append(i)

            if i - queue[0] + 1 == target:
                queue.popleft()
                cnt += 1

    elif s == "O":
        if I_flag:  # IO
            I_flag = False
        else:  # OO
            queue.clear()

print(cnt)
