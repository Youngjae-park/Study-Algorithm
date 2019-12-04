T = int(input())

class ball():
    def __init__(self, x, y, direction, start_i, start_j, score, finish = False):
        self.i = i
        self.j = j
        self.start_i = start_i
        self.start_j = start_j
        self.direction = direction
        self.score = score
        self.finish = finish
        
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
dir_ = ((-1,0),(1,0),(0,-1),(0,1))

def find_pair(i_i, j_j, num):
    a = num
    for i in range(N):
        for j in range(N):
            if board[i][j] == a:
                if i_i != i and j_j != j:
                    return (i, j)

def move(ball):
    if not ball.finish:
        if ball.direction == UP:
            for i in range(ball.i-1,-1,-1):
                if i == 0: # 벽 부딪힐 때
                    if board[i][ball.j] == 0:
                        ball.direction = DOWN
                        ball.score += 1
                        ball.i = i
                        break
                    else: # 그 외
                        if board[i][ball.j] == -1 or i == ball.start_i:
                            score.append(ball.score)
                            ball.finish = True
                            return
                        if 5 < board[i][ball.j] < 11:
                            new_i, new_j = find_pair(i, ball.j, board[i][ball.j])
                            ball.i = new_i
                            ball.j = new_j
                        if board[i][ball.j] == 1 and board[i][ball.j] == 4 and board[i][ball.j] ==5:
                            ball.i = i
                            ball.score += 1
                            ball.direction = DOWN
                            break
                        if board[i][ball.j] == 2:
                            ball.i = i
                            ball.score += 1
                            ball.direction = RIGHT
                            break
                        if board[i][ball.j] == 3:
                            ball.i = i
                            ball.score += 1
                            ball.direction = LEFT
                            break
                else:
                    if board[i][ball.j] == -1 or i == ball.start_i:
                        score.append(ball.score)
                        ball.finish = True
                        return
                    if 5 < board[i][ball.j] < 11:
                        new_i, new_j = find_pair(i, ball.j, board[i][ball.j])
                        ball.i = new_i
                        ball.j = new_j                    
                    if board[i][ball.j] == 1 and board[i][ball.j] == 4 and board[i][ball.j] ==5:
                        ball.i = i
                        ball.score += 1
                        ball.direction = DOWN
                        break
                    if board[i][ball.j] == 2:
                        ball.i = i
                        ball.score += 1
                        ball.direction = RIGHT
                        break
                    if board[i][ball.j] == 3:
                        ball.i = i
                        ball.score += 1
                        ball.direction = LEFT
                        break
                            
        if ball.direction == DOWN:
            for i in range(ball.i+1,N,1):
                if i == N-1: # 벽 부딪힐 때
                    if board[i][ball.j] == 0:
                        ball.direction = UP
                        ball.score += 1
                        ball.i = i
                        break
                    else: # 그 외
                        if board[i][ball.j] == -1 or i == ball.start_i:
                            score.append(ball.score)
                            ball.finish = True
                            return
                        if 5 < board[i][ball.j] < 11:
                            new_i, new_j = find_pair(i, ball.j, board[i][ball.j])
                            ball.i = new_i
                            ball.j = new_j
                        if board[i][ball.j] == 2 and board[i][ball.j] == 3 and board[i][ball.j] ==5:
                            ball.i = i
                            ball.score += 1
                            ball.direction = UP
                            break
                        if board[i][ball.j] == 1:
                            ball.i = i
                            ball.score += 1
                            ball.direction = RIGHT
                            break
                        if board[i][ball.j] == 4:
                            ball.i = i
                            ball.score += 1
                            ball.direction = LEFT
                            break
                else:
                    if board[i][ball.j] == -1 or i == ball.start_i:
                        score.append(ball.score)
                        ball.finish = True
                        return
                    if 5 < board[i][ball.j] < 11:
                        new_i, new_j = find_pair(i, ball.j, board[i][ball.j])
                        ball.i = new_i
                        ball.j = new_j                    
                    if board[i][ball.j] == 1 and board[i][ball.j] == 4 and board[i][ball.j] ==5:
                        ball.i = i
                        ball.score += 1
                        ball.direction = DOWN
                        break
                    if board[i][ball.j] == 2:
                        ball.i = i
                        ball.score += 1
                        ball.direction = RIGHT
                        break
                    if board[i][ball.j] == 3:
                        ball.i = i
                        ball.score += 1
                        ball.direction = LEFT
                        break

        if ball.direction == LEFT:
            for j in range(ball.j-1,-1,-1):
                if j == 0: # 벽 부딪힐 때
                    if board[ball.i][j] == 0:
                        ball.direction = RIGHT
                        ball.score += 1
                        ball.j = j
                        break
                    else: # 그 외
                        if board[ball.i][j] == -1 or j == ball.start_j:
                            score.append(ball.score)
                            ball.finish = True
                            return
                        if 5 < board[ball.i][j] < 11:
                            new_i, new_j = find_pair(ball.i, j, board[ball.i][j])
                            ball.i = new_i
                            ball.j = new_j
                        if board[ball.i][j] == 3 and board[ball.i][j] == 4 and board[ball.i][j] ==5:
                            ball.j = j
                            ball.score += 1
                            ball.direction = RIGHT
                            break
                        if board[ball.i][j] == 1:
                            ball.j = j
                            ball.score += 1
                            ball.direction = UP
                            break
                        if board[ball.i][j] == 2:
                            ball.j = j
                            ball.score += 1
                            ball.direction = DOWN
                            break
                else:
                    if board[ball.i][j] == -1 or j == ball.start_j:
                        score.append(ball.score)
                        ball.finish = True
                        return
                    if 5 < board[ball.i][j] < 11:
                        new_i, new_j = find_pair(ball.i, j, board[ball.i][j])
                        ball.i = new_i
                        ball.j = new_j                    
                    if board[ball.i][j] == 3 and board[ball.i][j] == 4 and board[ball.i][j] ==5:
                        ball.j = j
                        ball.score += 1
                        ball.direction = RIGHT
                        break
                    if board[ball.i][j] == 1:
                        ball.j = j
                        ball.score += 1
                        ball.direction = UP
                        break
                    if board[ball.i][j] == 2:
                        ball.j = j
                        ball.score += 1
                        ball.direction = DOWN
                        break
                    
        if ball.direction == RIGHT:
            for j in range(ball.j+1,N-1,1):
                if j == N-1: # 벽 부딪힐 때
                    if board[ball.i][j] == N-1:
                        ball.direction = LEFT
                        ball.score += 1
                        ball.j = j
                        break
                    else: # 그 외
                        if board[ball.i][j] == -1 or j == ball.start_j:
                            score.append(ball.score)
                            ball.finish = True
                            return
                        if 5 < board[ball.i][j] < 11:
                            new_i, new_j = find_pair(ball.i, j, board[ball.i][j])
                            ball.i = new_i
                            ball.j = new_j
                        if board[ball.i][j] == 1 and board[ball.i][j] == 2 and board[ball.i][j] ==5:
                            ball.j = j
                            ball.score += 1
                            ball.direction = LEFT
                            break
                        if board[ball.i][j] == 3:
                            ball.j = j
                            ball.score += 1
                            ball.direction = DOWN
                            break
                        if board[i][ball.j] == 4:
                            ball.j = j
                            ball.score += 1
                            ball.direction = UP
                            break
                else:
                    if board[ball.i][j] == -1 or j == ball.start_j:
                        score.append(ball.score)
                        ball.finish = True
                        return
                    if 5 < board[ball.i][j] < 11:
                        new_i, new_j = find_pair(ball.i, j, board[ball.i][j])
                        ball.i = new_i
                        ball.j = new_j                    
                    if board[ball.i][j] == 1 and board[ball.i][j] == 2 and board[ball.i][j] ==5:
                        ball.j = j
                        ball.score += 1
                        ball.direction = LEFT
                        break
                    if board[ball.i][j] == 3:
                        ball.j = j
                        ball.score += 1
                        ball.direction = DOWN
                        break
                    if board[ball.i][j] == 4:
                        ball.j = j
                        ball.score += 1
                        ball.direction = UP
                        break
        return ball
    else:
        return 0
    
                    

for test_case in range(1, T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    queue = []
    score = []

    for i in range(N):
        board[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                queue.append(ball(i,j, UP, i, j, 0))
                queue.append(ball(i,j, DOWN, i, j, 0))
                queue.append(ball(i,j, LEFT, i, j, 0))
                queue.append(ball(i,j, RIGHT, i, j, 0))

    queue.pop(0)
    while queue:
        temp = queue.pop(0)
        x = move(temp)
        if x == 0:
            pass
        else:
            queue.append(x)

    print(max(score))
    
    

    





















''' input
1
10
0 1 0 3 0 0 0 0 7 0
0 0 0 0 -1 0 5 0 0 0
0 4 0 0 0 3 0 0 2 2
1 0 0 0 1 0 0 3 0 0
0 0 3 0 0 0 0 0 6 0
3 0 0 0 2 0 0 1 0 0
0 0 0 0 0 1 0 0 4 0
0 5 0 4 1 0 7 0 0 5
0 0 0 0 0 1 0 0 0 0
2 0 6 0 0 4 0 0 0 4
'''
