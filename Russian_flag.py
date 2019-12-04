T = int(input())

def find(W,B,R):
    global min_
    sum_ = 0
    for W_r in range(W):
        for j in range(M):
            if flag[W_r][j] != 'W':
                sum_ += 1
        if sum_>min_:
            return
    for B_r in range(W,W+B):
        for j in range(M):
            if flag[B_r][j] != 'B':
                sum_ += 1
        if sum_>min_:
            return
    for R_r in range(W+B,W+B+R):
        for j in range(M):
            if flag[R_r][j] != 'R':
                sum_ += 1
        if sum_>min_:
            return

    if sum_ < min_:
        min_ = sum_

    return

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    flag = list(list(input()) for _ in range(N))
    min_ = N*M

    for W in range(1, N-1):
        for B in range(1, N-1):
            for R in range(1, N-1):
                if W+B+R == N:
                    find(W,B,R)

    print("#{} {}".format(test_case, min_))
                    
