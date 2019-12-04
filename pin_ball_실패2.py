T = int(input())

#ball class
class ball():
    def __init__(self, i, j, direction, score, flag = False):
        self.i = i
        self.j = j
        self.direction = direction
        self.score = score
        self.flag = flag

def change(ball, num):
    if num == -1:
        ball.flag = True
        pass
    elif num == 0:
        ball.score = 2*ball.score + 1
        ball.flag = True
    #wormhole
    elif 5 < num < 11:
        for i,j in wormhole[num-6]:
            if i != ball.i and j != ball.j:
                ball.i = i
                ball.j = j
        
    #change direction
    else:
        if ball.direction == UP:
            if num in (1,4,5):
                ball.direction = DOWN
                ball.score = 2*ball.score + 1
                ball.flag = True
            elif num == 2:
                ball.direction = RIGHT
                ball.score += 1
            elif num == 3:
                ball.direction = LEFT
                ball.score += 1
        if ball.direction == DOWN:
            if num in (2,3,5):
                ball.direction = UP
                ball.score = 2*ball.score + 1
                ball.flag = True
            elif num == 1:
                ball.direction = RIGHT
                ball.score += 1
            elif num == 4:
                ball.direction = LEFT
                ball.score += 1
        if ball.direction == LEFT:
            if num in (3,4,5):
                ball.direction = RIGHT
                ball.score = 2*ball.score + 1
                ball.flag = True
            elif num == 1:
                ball.direction = UP
                ball.score += 1
            elif num == 2:
                ball.direction = DOWN
                ball.score += 1
        if ball.direction == RIGHT:
            if num in (1,2,5):
                ball.direction = LEFT
                ball.score = 2*ball.score + 1
                ball.flag = True
            elif num == 3:
                ball.direction = DOWN
                ball.score += 1
            elif num == 4:
                ball.direction = UP
                ball.score += 1
    return ball    

def finding(ball):
    f_flag = False
    if ball.direction == UP:
        for di in range(ball.i-1, -1, -1):
            if board[di][ball.j] != 0:
                f_flag = True
                return (di, ball.j)
            if di == 0:
                f_flag = True
                return (di, ball.j)
        if f_flag == False:
            ball.flag = True
            return (ball.i, ball.j)
    if ball.direction == DOWN:
        for di in range(ball.i+1, N, 1):
            if board[di][ball.j] != 0:
                f_flag = True
                return (di, ball.j)
            if di == N-1:
                f_flag = True
                return (di, ball.j)
        if f_flag == False:
            ball.flag = True
            return (ball.i, ball.j)
    if ball.direction == LEFT:
        for dj in range(ball.j-1, -1, -1):
            if board[ball.i][dj] != 0:
                f_flag = True
                return (ball.i, dj)
            if dj == 0:
                f_flag = True
                return (ball.i, dj)
        if f_flag == False:
            ball.flag = True
            return (ball.i, ball.j)
    if ball.direction == RIGHT:
        for dj in range(ball.j+1, N-1, 1):
            if board[ball.i][dj] != 0:
                f_flag = True
                return (ball.i, dj)
            if dj == N-1:
                f_flag = True
                return (ball.i, dj)
        if f_flag == False:
            ball.flag = True
            return (ball.i, ball.j)
                
                

#direction tuple and initializing direction word
dir_ = ((-1,0),(1,0),(0,-1),(0,1))
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

for test_case in range(1, T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    stack = []
    wormhole = [0]*5
    score_list = []
    for i in range(5):
        wormhole[i] = []
    
    #initialize board array
    for i in range(N):
        board[i] = list(map(int, input().split()))

    #stack start_ball
    for i in range(N):
        for j in range(N):
            if board[i][j] == 6:
                wormhole[0].append([i,j])
            if board[i][j] == 7:
                wormhole[1].append([i,j])
            if board[i][j] == 8:
                wormhole[2].append((i,j))
            if board[i][j] == 9:
                wormhole[3].append((i,j))
            if board[i][j] == 10:
                wromhole[4].append((i,j))
            if board[i][j] == 0:
                for d in range(4):
                    stack.append(ball(i, j, d, 0))

    while stack:
        temp = stack.pop()
        print(len(stack))
        print(temp.i, temp.j, temp.score, temp.direction, temp.flag)
        if temp.flag == True:
            score_list.append(temp.score)
        new_i, new_j = finding(temp)
        new_temp = change(temp, board[new_i][new_j])
        if new_temp.flag == False:
            stack.append(new_temp)
