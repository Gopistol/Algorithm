import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
a = [0 for _ in range(10 ** 5 + 1)]


def front_search(node):
    front = node + 1

    if front < len(a) and not a[front]:
        a[front] = a[node] + 1
        return front

    return -1


def back_search(node):
    back = node - 1

    if back > 0 and not a[back]:
        a[back] = a[node] + 1
        return back

    return -1


def flash_search(node):
    flash = node * 2

    if flash < len(a) and not a[flash]:
        a[flash] = a[node] + 1
        return flash

    return -1


def bfs_bottom_up(n, k):
    queue = deque()
    queue.append(n)
    a[n] = 0  # 시간

    while queue:
        node = queue.popleft()

        front = front_search(node)
        back = back_search(node)
        flash = flash_search(node)

        for p in (front, back, flash):
            if p == k:
                return a[k]

        if front > 0:
            queue.append(front)
        if back > 0:
            queue.append(back)
        if flash > 0:
            queue.append(flash)

    return a[k]


if n < k:
    print(bfs_bottom_up(n, k))
else:
    print(n - k)
