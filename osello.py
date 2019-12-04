T = int(input())

dir_ = ((-1,0),(0,1),(1,0),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1))

def step(i, j, color, direction, change):
    di, dj = dir_[direction]
    ni = i + di
    nj = j + dj
    if -1<ni<N and -1<nj<N:
        if board[ni][nj] == 0:
            return
        elif board[ni][nj] != color:
            change.append([ni,nj])
            step(ni,nj,color,direction,change)
        elif board[ni][nj] == color:
            if len(change):
                while change:
                    ti, tj = change.pop()
                    board[ti][tj] = color
                return
            return
    else:
        return
    

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for __ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    stack = list(list(map(int, input().split())) for _ in range(M))

    for _ in range(M):
        j, i, color = stack.pop(0)
        i -= 1
        j -= 1
        board[i][j] = color
        for i_dir in range(len(dir_)):
            step(i, j, color, i_dir, [])

    num_black = 0
    num_white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                num_black += 1
            elif board[i][j] == 2:
                num_white += 1

    print("#{} {} {}".format(test_case, num_black, num_white))

        
