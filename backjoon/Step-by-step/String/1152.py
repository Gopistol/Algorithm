import sys

input = sys.stdin.readline

word = str(input().rstrip('\n'))
check = [0 for _ in range(26)]
# 모두 대문자로 변환
word = word.upper()
# A ~ Z 까지 돌며 26칸짜리 정수형 배열에 횟수 체크
for i in range(65, 91, 1):
    for j in range(len(word)):
        if chr(i) == word[j]:
            check[i-65] += 1

# 정수형 배열의 최댓값과 그 인덱스 찾아서 출력
if check.count(max(check)) != 1:
    print('?')
else:
    print(chr(check.index(max(check)) + 65))
