from collections import deque

def bfs(num):
    queue = deque([num])
    while queue:
        num = queue.popleft()
        if num == k:
            return count[num]
        for next_num in (num - 1, num + 1, num * 2):
            if 0 <= next_num <= 100000 and not count[next_num]:
                count[next_num] = count[num] + 1
                queue.append(next_num)


n, k = map(int, input().split())
count = [0] * 100001
print(bfs(n))