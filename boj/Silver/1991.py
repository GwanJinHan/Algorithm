import sys
input = sys.stdin.readline

n = int(input())
d = {}
for _ in range(n):
    a, b, c = input().rstrip().split()
    d[a] = [b, c]

def preorder(n):
    if n == ".":
        return
    print(n, end="")
    preorder(d[n][0])
    preorder(d[n][1])

def inorder(n):
    if n == ".":
        return
    inorder(d[n][0])
    print(n, end="")
    inorder(d[n][1])

def postorder(n):
    if n == ".":
        return
    postorder(d[n][0])
    postorder(d[n][1])
    print(n, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
