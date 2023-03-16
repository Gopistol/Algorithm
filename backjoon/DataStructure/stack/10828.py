import sys

input = sys.stdin.readline

stack = []
count = int(input().rstrip('\n'))
for _ in range(count):
    command = (list(map(str, input().rstrip('\n').split())))
    if command[0] == 'push':  # push X 명령을 받는 경우
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
    command.clear()  # command 배열 비우기
