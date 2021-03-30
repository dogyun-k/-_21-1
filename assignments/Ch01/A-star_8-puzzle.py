import queue

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
    
    def f(self):
        return self.h() + self.g()
    
    def h(self):
        return (sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)]))
    
    def g(self):
        return self.moves

    def __lt__(self, other):
        return self.f() < other.f()
    
    def __str__(self):
        return "---------- f(n) = " + str(self.f()) + "\n---------- h(n) = " + str(self.h()) + "\n---------- g(n) = " + str(self.g()) + "\n" +str(self.board[:3]) +"\n"+str(self.board[3:6]) +"\n"+str(self.board[6:]) +"\n"+"----------"


puzzle = [
    1, 2, 3,
    4, 5, 6,
    0, 7, 8
]

goal = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]


open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle, goal))

closed_queue = []
moves = 0
check = 0

while not open_queue.empty():

    current = open_queue.get()
    print(current)

    if current.board == goal:
        print("탐색 성공")
        break

    moves = current.moves + 1

    for state in current.expand(moves):

        for i in closed_queue:
            if state.board == i.board:
                check = 1

        if check != 1:
            open_queue.put(state)
    
        check = 0
        
    closed_queue.append(current)
    
else:
    print("탐색 실패")