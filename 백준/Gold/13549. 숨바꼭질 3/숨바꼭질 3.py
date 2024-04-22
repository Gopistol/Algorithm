import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

d = list(-1 for _ in range(10 ** 5 + 1))


def flash(node, q):
    t = node * 2
    if t > len(d):
        return
    if t < k * 2 and d[t] == -1:
        d[t] = d[node]
        q.append(t)
        return t


def bfs(n, k):
    d[n] = 0
    q = deque()
    q.append(n)

    while q:
        node = q.popleft()

        if flash(node, q) == k:
            return d[k]

        # 후진
        b = node - 1
        if d[b] == -1 and 0 < b <= k or d[b] > d[node]:
            d[b] = d[node] + 1
            q.append(b)

        # 전진
        f = node + 1
        if f < len(d) and d[f] == -1 and f <= k:
            d[f] = d[node] + 1
            q.append(f)
            
    return d[k]


if n > k:
    print(n - k)
else:
    print(bfs(n, k))
