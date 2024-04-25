import sys
n, m = map(int, sys.stdin.readline().split())
last = int(m ** 0.5)
arr = [1] * (m - n + 1) 
i = 2
while i <= last:
    sqr = i ** 2
    num = (n // sqr) * sqr
    while num <= m:
        if n <= num <= m:
            arr[num - n] = 0
        num += sqr
    i += 1
print(sum(arr))
