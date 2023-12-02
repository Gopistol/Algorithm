import math

def check_tree_property(str_number, index, level):
    # 기본 케이스: 리프 노드에서 멈춘다.
    if level <= 1:
        return True

    half = 2 ** (level - 2)
    left_child_index = index - half
    right_child_index = index + half

    # 부모 노드가 '0'이 되면 자식이 '1'이면 안 된다.
    if str_number[index] == '0' and ('1' in [str_number[left_child_index], str_number[right_child_index]]):
        return False

    # 재귀적으로 왼쪽과 오른쪽 자식을 탐색한다.
    return check_tree_property(str_number, left_child_index, level - 1) and \
        check_tree_property(str_number, right_child_index, level - 1)


def is_full_binary_tree(binary_str):
    length = len(binary_str)
    levels = int(math.log(length, 2)) + 1

    # 바이너리의 길이를 제곱수로 만든다.
    padded_length = 2 ** levels - 1
    binary_str = binary_str.rjust(padded_length, '0')

    # 루트 노드가 '1'인지 확인
    root_index = (padded_length // 2)
    if binary_str[root_index] != '1':
        return 0

    return 1 if check_tree_property(binary_str, root_index, levels) else 0


def solution(numbers):
    return [is_full_binary_tree(bin(number)[2:]) for number in numbers]

