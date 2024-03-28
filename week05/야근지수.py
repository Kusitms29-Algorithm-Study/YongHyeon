import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    arr = [-w for w in works]
    heapq.heapify(arr)

    for _ in range(n):
        heapq.heappush(arr, heapq.heappop(arr) + 1)

    return sum([a ** 2 for a in arr])
