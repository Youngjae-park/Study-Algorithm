T = int(input())

dir_ = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

def check(i, j):
    global map_
    cnt = 0
    if(map_[i][j] == '*'):
        return
    for di, dj in dir_:
        ni = i + di
        nj = j + dj
        if -1<ni<N and -1<nj<N:
            if(map_[ni][nj]=='*'):
                cnt += 1
    map_[i][j] = cnt
    return

def click(i, j):
    global min_
    if(map_[i][j]==0):
        return True
    if(map_[i][j] == '*'):
        # print("i, j is *")
        return False
    for di, dj in dir_:
        ni = i + di
        nj = j + dj
        if -1<ni<N and -1<nj<N:
            if(map_[ni][nj] == 0):
                return False
    min_ += 1
    return False

def zero(i, j):
    global zero_
    global visited
    global min_
    if (i, j) in zero_:
        return
    else:
        queue = []
        queue.append((i,j))
        zero_.append((i,j))
        while(queue):
            qi, qj = queue.pop(0)
            visited[qi][qj] = True
            for di, dj in dir_:
                ni = qi + di
                nj = qj + dj
                if(-1<ni<N and -1<nj<N):
                    if(map_[ni][nj]==0 and not visited[ni][nj]):
                        queue.append((ni, nj))
                        zero_.append((ni, nj))
                        visited[ni][nj] = True
        min_ += 1
        return

for test_case in range(1, T+1):
    N = int(input())
    map_ = list(list(input()) for _ in range(N))
    visited = list([False for _ in range(N)] for __ in range(N))
    zero_ = []

    min_ = 0

    for i in range(N):
        for j in range(N):
            check(i, j)

    for i in range(N):
        for j in range(N):
            if(click(i, j)):
                zero(i, j)
            # print(i, j, "min_ : ", min_)

    # print(map_)

    print("#{} {}".format(test_case, min_))


