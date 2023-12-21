from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a - 1].append((b - 1, c))
    tree[b - 1].append((a - 1, c))


def bfs(start, end):
    visit = set()

    queue = deque([(start, 0)])

    while queue:
        cur_node, cur_weight = queue.popleft()

        if cur_node in visit:
            continue
        if cur_node == end:
            return cur_weight
        visit.add(cur_node)

        for node, weight in tree[cur_node]:
            if node not in visit:
                queue.append((node, cur_weight + weight))


for _ in range(m):
    start, end = map(int, input().split())
    print(bfs(start - 1, end - 1))
