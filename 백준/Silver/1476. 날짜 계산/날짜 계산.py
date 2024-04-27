import sys

input = sys.stdin.readline

e, s, m = map(int, input().split())
a, b, c, y = 1, 1, 1, 1

while (e, s, m) != (a, b, c):
    a += 1
    b += 1
    c += 1
    y += 1
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1

print(y)
