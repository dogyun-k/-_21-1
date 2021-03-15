# CH1- BFS search 을 이용한 8-puzzle problem

class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    def get_new_board(self, i1, i2, moves):     # 두 자리 바꾸고 바꾼 보드 리턴
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]

        return State(new_board, self.goal, moves)

    def expand(self, moves):
        result = []

        i = self.board.index(0)     # 빈자리의 위치 뽑기

        if not i in [0, 1, 2]:      # 맨 위에 줄에 있는게 아니면 위로 이동
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6]:      # 맨 왼쪽 줄에 있는게 아니면 왼쪽 이동
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]:      # 맨 오른쪽 줄에 있는게 아니면 오른쪽 이동
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:      # 맨 아래 줄에 있는게 아니면 아래 이동
            result.append(self.get_new_board(i, i+3, moves))
        
        return result       # 맨 처음 0의 위치에서 이동할 수 있는 모든 경우의 수를 담은 리스트 리턴(확장 가능한 모든 경우의 수 리턴)
    
    def __str__(self):
        return str(self.board[:3]) +"\n"+str(self.board[3:6]) +"\n"+str(self.board[6:]) +"\n"+"----------------------"

puzzle = [
    1, 2, 3,
    0, 5, 6,
    4, 7, 8
]

goal = [
    1, 2, 3, 
    4, 5, 6, 
    7, 8, 0
]


open_queue = []
open_queue.append(State(puzzle, goal))

closed_queue = []
moves = 0
check = 0

while len(open_queue) != 0:
    current = open_queue.pop(0)		# 맨 앞에꺼 빼기 (큐)
    print(current)

    if current.board == goal:
        print("탐색 성공")
        break

    moves = current.moves + 1
    closed_queue.append(current)

    for state in current.expand(moves):

        for i in (closed_queue + open_queue):
            if state.board == i.board:
                check = 1
                break

        if check != 1:
            open_queue.append(state)

        check = 0