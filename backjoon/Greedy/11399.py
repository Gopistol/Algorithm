import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
line = list(map(int, input().split()))
line.sort()
time = 0
for i in range(n):
    for j in range(n):
        if i >= j:
            time += line[j]
print(time)
