T = int(input())

ewsn = [(0, 0, 1),(1, 0, -1),(2, 1, 0),(3, -1, 0)]
direction = [0, [1,3,0,2],[1,2,3,0],[2,0,3,1],[3,0,1,2],[1,0,3,2]]

for test_case in range(1, T+1):
    N = int(input())
    board = [[] for _ in range(N+2)]
    wormhole = [[] for _ in range(5)]

    for i in range(0, N+2):
        if i == 0 or i == N+1:
            board[i] = [5]*(N+2)
        else:
            board[i].append(5)
            board[i].extend(list(map(int, input().split())))
            board[i].append(5)
    
    
    for i in range(1,N+1):
        for j in range(1,N+1):
            if 5< board[i][j] <11:
                idx_wormhole = board[i][j] - 6
                wormhole[idx_wormhole].append((i,j))

    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 0:
                for k in range(4):
                    #print(board)
                    s_i, s_j = i, j
                    dn, di, dj = ewsn[k]
                    ni = i + di
                    nj = j + dj
                    cnt = 0
                    #print(s_i, s_j)
                    while True:
                        #print(dn, ni, nj, board[ni][nj])
                        if board[ni][nj] == -1 or [s_i, s_j] == [ni, nj]:
                            if ans< cnt:
                                ans = cnt
                            break
                        elif 0< board[ni][nj] <6:
                            cnt += 1
                            dn, di, dj = ewsn[direction[board[ni][nj]][dn]]
                        elif 5< board[ni][nj] <11:
                            if (ni, nj) == wormhole[board[ni][nj]-6][0]:
                                ni, nj = wormhole[board[ni][nj]-6][1]
                            else:
                                ni, nj = wormhole[board[ni][nj]-6][0]
                        ni += di
                        nj += dj

    print("#{} {}".format(test_case, ans))
