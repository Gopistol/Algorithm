import sys
input = sys.stdin.readline

count = int(input().rstrip('\n'))
isGroupWord = count

for _ in range(count):
    word = str(input().rstrip('\n'))
    # 그룹 단어인지 판별 - 알파벳 길이만큼의 불리언 배열 만들기
    isDuplicated = [False for _ in range(26)]
    for i in range(len(word)):
        alphabet = word[i]
        alphabetIndex = ord(alphabet) - 97
        if isDuplicated[alphabetIndex]: # 한 번 나왔던 알파벳일 경우
            if alphabet == word[i - 1]:
                continue
            else:
                isGroupWord -= 1
                break
        if not isDuplicated[alphabetIndex]:
            isDuplicated[alphabetIndex] = True # 처음 나오는 알파벳일 경우
print(isGroupWord)
