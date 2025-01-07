from collections import Counter as ct, defaultdict

board = [[".",".","1",".",".",".","3",".","."],
         [".",".","4",".",".",".","1",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".","8",".",".",".","."],
         [".","1",".",".","2",".",".",".","."],
         [".",".",".",".",".",".","6","3","."],
         ["7",".",".",".",".",".",".",".","."],
         ["5","8",".",".",".",".","4",".","."],
         [".","5",".",".","4",".",".",".","8"]]


col = [*zip(*board)]
for i in range(len(board)):
    row = ct(board[i])
    col1 = ct(col[i])
    if row['.'] + (len(row.keys())-1) != 9 or col1['.'] + (len(col1.keys())-1) != 9:
        print(False)
i = c = 0
while c < 9:
    top = set(board[c][i:i + 3])
    mid = set(board[c + 1][i:i + 3])
    down = set(board[c + 2][i:i + 3])
    res = (top & mid) ^ (mid & down) ^ (top & down)
    print(res)
    if res != set(".") or not res:
        print(False)
    if i >= 6:
        i = 0
        c+=3
    else:
        i+=3
