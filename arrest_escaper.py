T = int(input())

dir_ = [[], [[-1,0],[0,1],[1,0],[0,-1]], [[-1,0],[1,0]], [[0,1],[0,-1]], [[-1,0],[0,1]], [[0,1],[1,0]], [[1,0],[0,-1]], [[0,-1],[-1,0]]]

def solve(i, j, cnt, checked, dir_n):
    global total_check
    #print(i,j,cnt)
    if cnt == L:
        return
    for di, dj in dir_[dir_n]:
        ni = i + di
        nj = j + dj
        if -1<ni<N and -1<nj<M and not checked[ni][nj] and underground[ni][nj]:
            checked[ni][nj] = True
            if [-di,-dj] in dir_[underground[ni][nj]]:                                                 
                total_check[ni][nj] = True
                solve(ni,nj,cnt+1,checked, underground[ni][nj])
            checked[ni][nj] = False
            
            
    

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    total_check = [[False for _ in range(M)] for __ in range(N)]
    check = [[False for _ in range(M)] for __ in range(N)]

    check[R][C] = True
    total_check[R][C] = True
    solve(R,C,1,check,underground[R][C])
    sum_ = sum(1 for a in total_check for b in a if b)

    print("#{} {}".format(test_case,sum_))
