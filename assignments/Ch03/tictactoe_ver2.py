game_board = [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ']


def empty_cells(board):
    cells = []
    for x, cell in enumerate(board):
        if cell == ' ':
            cells.append(x)
    return cells

def valid_move(x):
    return x in empty_cells(game_board)

def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

def draw(board):
    for i in range(0, len(board), 3):
        print("-------------\t-------------")
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |", end='\t')
        print(f"| {i} | {i+1} | {i+2} |")
    print("-------------\t--------------")

def evaluate(board):
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score

def check_win(board, player):
    win_conf = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conf

def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')

def minimax(board, depth, maxPlayer):
    pos = -1

    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)
    
    if maxPlayer:
        value = -10000

        for p in empty_cells(board):
            board[p] = 'X'

            # 경기자를 교체하여서 imnimax()를 순환호출한다.
            x, score = minimax(board, depth-1, False)
            board[p] = ' ' # 보드는 원 상태로 돌린다.
            if score > value:
                value = score # 최대값을 취한다.
                pos = p # 최대값의 위치를 기억한다.

    else:
        value = +10000

        for p in empty_cells(board):
            board[p] = 'O'
            
            # 경기자를 교체하여서 imnimax()를 순환호출한다.
            x, score = minimax(board, depth-1, True)
            board[p] = ' ' # 보드는 원 상태로 돌린다.
            if score < value:
                value = score # 최소값을 취한다.
                pos = p # 최소값의 위치를 기억한다.

    return pos, value # 위치와 값을 반환한다.



player = 'X'
computer = 'O'

# 메인 프로그램
while True:
    draw(game_board)
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break

    while True:
        you = int(input("당신 차례 : "))
        if move(you, player):
            break

    i, v = minimax(game_board, 9, computer=='X')
    move(i, computer)


# 결과
if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')
