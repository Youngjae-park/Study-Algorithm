T = int(input())

def dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def solve(A_x, A_y, B_x, B_y, move_A, move_B, charge, t):
    global ans
    BC_A = [0]*A
    BC_B = [0]*A
    #first check, later next func
    for i in range(A):
        if dist(A_x, A_y, BC[i][0], BC[i][1])<=BC[i][2]:
            BC_A[i] = BC[i][3]
        if dist(B_x, B_y, BC[i][0], BC[i][1])<=BC[i][2]:
            BC_B[i] = BC[i][3]
                
    max_ = 0
    idx_A = 0
    idx_B = 0
    for i in range(A):
        for j in range(A):
            tot = BC_A[i] + BC_B[j]
            if i==j and BC_A[i]==BC_B[j]:
                tot = tot//2
            if tot>max_:
                max_ = tot
                idx_A = i
                idx_B = j
                
            
    #t 마다 charge_A, charge_B 확인하고 싶을 때
    ans += max_
    #print(BC_A, BC_B)
    #print("{} -> {} {} {}".format(t, BC_A[idx_A], BC_B[idx_B], charge), "좌표" ,A_x, A_y, B_x, B_y)

    if t == N:
        return
    #좌표 이동
    dx, dy = dir_[move_A.pop(0)]
    A_x += dx
    A_y += dy
    dx, dy = dir_[move_B.pop(0)]
    B_x += dx
    B_y += dy
    solve(A_x, A_y, B_x, B_y, move_A, move_B, charge, t+1)
    
            
            

dir_ = ((0,0), (0,-1), (1,0), (0,1), (-1,0))

for test_case in range(1, T+1):
    N, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    BC = []
    
    for _ in range(A):
        BC.append(tuple(map(int, input().split()))) #(X, Y, C, P)

    ans = 0
    solve(1,1,10,10,move_A,move_B,0,0)
    
    print("#{} {}".format(test_case, ans))

    







'''input
1
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
'''
