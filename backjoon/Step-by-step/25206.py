import sys
input = sys.stdin.readline

grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
sum_grade = 0
sum_grade_score = 0
while(True):
    data = input().rstrip('\n')
    if data == '':
        break
    data = list(map(str, data.split()))
    credit = float(data[1])
    if data[2] == 'P':
        continue
    else:
        sum_grade += credit
        sum_grade_score += score[grade.index(data[2])] * credit
print(f'{sum_grade_score / sum_grade:.6f}')
