import sys
print(*sorted(sys.stdin.readline().rstrip(),reverse=True),sep='')