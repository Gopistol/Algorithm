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


def bfs(n, k):
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
            if p > 0:
                queue.append(p)

    return a[k]


if n < k:
    print(bfs(n, k))
else:
    print(n - k)

routes = []

a[n] = 0  # 시작 지점 초기화


def bottom_up(routes):
    target_index = k

    for count in range(a[k], 0, -1):

        if target_index + 1 < len(a) and a[target_index + 1] == count - 1:
            routes.append(target_index)
            target_index += 1
            continue

        if a[target_index - 1] == count - 1:
            routes.append(target_index)
            target_index -= 1
            continue

        if target_index % 2 == 0:
            index = int(target_index / 2)
            if a[index] == count - 1:
                routes.append(target_index)
                target_index = index

    routes.append(n)
    routes.reverse()
    return routes


if n < k:
    routes = bottom_up(routes)
    print(*routes)
else:
    for i in range(n, k - 1, -1):
        print(i, end=' ')
