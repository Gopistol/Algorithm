import sys


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())

arr = [i + 1 for i in range(n)]
index = 0

print('<', end='')
for i in range(n):
    index += k
    if index <= len(arr):
        print(arr[index - 1], end='')
    else:
        while index > len(arr):
            index -= len(arr)
        print(arr[index - 1], end='')
    arr.pop(index - 1)
    index -= 1
    if i != n - 1:
        print(', ', end='')
print('>', end='')

