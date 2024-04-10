import sys

input = sys.stdin.readline

n = int(input())

queue = []
answer = []
for _ in range(n):
    answer = input().split()
    command = answer[0]
    value = 0

    if len(answer) == 2:
        value = answer[1]

    if command == 'push':
        queue.append(value)

    if command == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if command == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            last = len(queue)
            print(queue[last - 1])

    if command == 'size':
        print(len(queue))

    if command == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            number = queue[0]
            queue.remove(queue[0])
            print(number)

    if command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

