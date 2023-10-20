def solution(board):
    w = len(board)
    h = len(board[0])
    a = [[0] * h for _ in range(w)]
    max_square = 0

    for i in range(w):
        for j in range(h):
            if board[i][j] == 1:
                if i > 0 and j > 0:
                    a[i][j] = min(a[i - 1][j], a[i][j - 1], a[i - 1][j - 1]) + 1
                else:
                    a[i][j] = 1
                max_square = max(max_square, a[i][j])

    return max_square ** 2
