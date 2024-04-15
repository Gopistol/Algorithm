import sys
print(*sorted(list(map(int, sys.stdin.readline().rstrip())), reverse=True), sep='')