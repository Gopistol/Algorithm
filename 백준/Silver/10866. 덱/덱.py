import sys

input = sys.stdin.readline

n = int(input())

deque = []
answer = []

for _ in range(n):
    answer = input().split()
    command = answer[0]
    value = 0

    if len(answer) == 2:
        value = answer[1]

    if command == 'push_front':
        if not deque:
            deque.append(value)
        else:
            deque.insert(0, value)

    if command == 'push_back':
        deque.append(value)

    if command == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque.pop(0))

    if command == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque.pop())

    if command == 'size':
        print(len(deque))

    if command == 'empty':
        if not deque:
            print(1)
        else:
            print(0)

    if command == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])

    if command == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[len(deque) - 1])
