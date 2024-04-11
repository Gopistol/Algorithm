import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

for i in range(10):
    count = result.count(str(i))
    print(count)