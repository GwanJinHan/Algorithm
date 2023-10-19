import heapq

n = int(input())
candidates = [int(input()) for _ in range(n)]
my_votes = candidates[0]
candidates = candidates[1:]

if n == 1:
    print(0)
else:
    heap = [-candidate for candidate in candidates]
    heapq.heapify(heap)

    count = 0
    while my_votes <= -heap[0]:
        max_votes = -heapq.heappop(heap)
        my_votes += 1
        count += 1
        heapq.heappush(heap, -max_votes + 1)

    print(count)
