import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
reversed_tree = {}

leaves = set(range(1, n + 1))
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    reversed_tree[b] = (a, c)
    if a in leaves:
        leaves.remove(a)

weights = [{} for _ in range(n)]


def search(child, acc=0):
    if child == 1:
        return

    parent, c = reversed_tree[child]
    acc += c

    try:
        weights[parent - 1][child] = max(weights[parent - 1][child], acc)
    except:
        weights[parent - 1][child] = acc

    return search(parent, acc)


for leaf in leaves:
    search(leaf)


ans = 0
for i in range(n):
    if len(weights[i]) > 2:
        t = sorted(weights[i].values())
        ans = max(ans, t[-1] + t[-2])
    else:
        ans = max(ans, sum(weights[i].values()))

print(ans)
