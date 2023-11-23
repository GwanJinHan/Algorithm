import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
tree = [[] for _ in range(n)]
weights = [[] for _ in range(n)]
visit = [False] * n


for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a - 1].append((b - 1, c))


def biggest(arr, elem):
    if len(arr) == 0:
        arr.append(elem)
    else:
        arr.append(elem)
        arr.sort(reverse=True)
        arr = [arr[0], arr[1]]
        

stack = deque([(c, w, 0) for c, w in tree[0]])


while stack:
    node, weight, par = stack.pop()

    if len(tree[node]) == 0:
        continue

    for nn, nw in tree[node]:
        stack.append((nn, weight + nw))