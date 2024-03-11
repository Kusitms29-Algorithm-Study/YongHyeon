import sys
from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque()

count = [0 for _ in range(F + 1)]

def bfs(num):
    queue.append(num)
    count[num] = 1

    while queue:
        floor = queue.popleft()

        if floor == G:
            return count[floor] - 1

        if floor + U <= F and count[floor + U] == 0:
            count[floor + U] = count[floor] + 1
            queue.append(floor + U)
        elif floor - D > 0 and count[floor - D] == 0:
            count[floor - D] = count[floor] + 1
            queue.append(floor - D)

    return "use the stairs"


result = bfs(S)

print(result)