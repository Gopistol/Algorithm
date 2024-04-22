import sys
s = int(sys.stdin.readline())
d = list(range(1002))
for i in range(2, s + 1):
    j = 2
    while i * j < 1002:
        d[i * j] = min(d[i * j], d[i] + j)
        d[i * j - 1] = min(d[i * j - 1], d[i * j] + 1)
        j += 1
print(d[s])
