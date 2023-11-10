x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ip1p3 = (y3 - y1) / (x3 - x1)

ip1p2 = (y2 - y1) / (x2 - x1)
ip2p3 = (y3 - y2) / (x3 - x2)

if ip1p2 > ip1p3 and ip2p3 < ip1p3:
    print(-1)
elif ip1p2 < ip1p3 and ip2p3 > ip1p3:
    print(1)
else:
    print(0)
