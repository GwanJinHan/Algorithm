# 해당 파티에 진실을 아는 사람이 있다면 => 반드시 그 파티에서는 진실 말함
# 그 파티에 있던 다른 사람들도 모두 진실을 알게 됨.
# BFS (QUEUE)
# Set 으로 구현하자
# 파티 별로 번호 매겨서 관리.
# 먼저 주어진 진실 아는 사람 모두 순회하며, 그 사람들이 포함된 파티의 나머지 인원 Q에 삽입, remove
# 또 파티를 돌며 Q 에 있는 인원이 들어있으면 나머지 사람 삽입 

# 탐색 마쳤을 때, 파티 목록에 남아있는 파티 수 출력
# 진실을 아는 사람 0명일때 => 바로 파티 개수 (m) 출력

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
truth_len, *truth_member = map(int, input().split())
truth_member = set(truth_member)
if truth_len == 0:
    print(m)
    sys.exit(0)

parties_idx = set(range(m))
parties = []
for i in range(m):
    _, *party = map(int, input().split())
    party = set(party)
    parties.append((i, party))

queue = deque(truth_member)

while queue:
    q = queue.popleft()
    if q in truth_member:
        continue
    for i, party in parties:
        if i in parties_idx and q in party:
            party.remove(q)
            queue.extend(party)
            truth_member.extend(party)
            parties_idx.remove(i)

print(len(parties_idx))