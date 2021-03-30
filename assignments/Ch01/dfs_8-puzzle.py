# CH1- DFS search 을 이용한 8-puzzle problem
import time

class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]

        return State(new_board, self.goal, moves)

    def expand(self, moves):
        result = []

        i = self.board.index(0)

        if not i in [0, 1, 2]:
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6]:
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i+3, moves))
        
        return result
    
    def __str__(self):
        return str(self.board[:3]) +"\n"+str(self.board[3:6]) +"\n"+str(self.board[6:]) +"\n----------"

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


open_stack = []         # 검사할 거 리스트
open_stack.append(State(puzzle, goal))  # 초기 보드 넣어주고

closed_stack = []       # 검사한 것 넣기
moves = 0
check = 0

while len(open_stack) != 0:
    current = open_stack.pop()     # 맨 뒤에꺼 뺴기 (스택)
    print(current)

    if current.board == goal:
        print("탐색 성공")
        break
 
    moves = current.moves + 1
    closed_stack.append(current)    # 검사 했으니 클로즈로 

    for state in current.expand(moves):

        if (state not in closed_stack) and (state not in open_stack):
            open_stack.append(state)
            
        for i in (closed_stack + open_stack):   # 검사했는지 안했는지 검사
            if state.board == i.board:
                check = 1
                break

        if check != 1:
            open_stack.append(state)

        check = 0
