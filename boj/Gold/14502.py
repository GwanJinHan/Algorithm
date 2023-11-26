from itertools import combinations
from collections import deque
import copy

def spread_virus(temp_lab, virus_positions, n, m):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    queue = deque(virus_positions)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append((nx, ny))

def get_safe_area(lab, n, m):
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                safe_area += 1
    return safe_area

def solve(n, m, lab):
    empty_spaces = []
    virus_positions = []

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                empty_spaces.append((i, j))
            elif lab[i][j] == 2:
                virus_positions.append((i, j))

    wall_combinations = list(combinations(empty_spaces, 3))
    max_safe_area = 0

    for walls in wall_combinations:
        temp_lab = copy.deepcopy(lab)

        for wall in walls:
            temp_lab[wall[0]][wall[1]] = 1

        spread_virus(temp_lab, virus_positions, n, m)
        safe_area = get_safe_area(temp_lab, n, m)

        max_safe_area = max(max_safe_area, safe_area)

    return max_safe_area

if __name__ == "__main__":
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]

    result = solve(n, m, lab)
    print(result)
