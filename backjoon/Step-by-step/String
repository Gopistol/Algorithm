import sys

input = sys.stdin.readline

case_count = int(input().rstrip('\n'))

for _ in range(case_count):
    count, string = map(str, input().rstrip('\n').split())
    newString = ''
    for i in range(len(string)):
        for _ in range(int(count)):
            newString += string[i]
    print(newString)
