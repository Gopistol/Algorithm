import sys

input = sys.stdin.readline
numbers = []
for _ in range(10):
    n = int(input().rstrip('\n'))
    n %= 42
    numbers.append(n)
duplicated = 0
for i in range(10):
    for j in range(10):
        if i < j:
            if numbers[i] == numbers[j]:
                duplicated += 1
                break

print(10 - duplicated)
