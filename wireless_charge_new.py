T = int(input())

def check(a_x, a_y, b_x, b_y):
    global total
    bc_check = []
    bc_a = []
    bc_b = []
    a = 0
    b = 0
    for i in range(A):
        if dist(a_x, a_y ,BC[i][0], BC[i][1]) <= BC[i][2] or dist(b_x, b_y, BC[i][0], BC[i][1]) <= BC[i][2]:
            bc_check.append(BC[i][3])
            if dist(a_x, a_y, BC[i][0], BC[i][1]) <= BC[i][2]:
                bc_a.append(BC[i][3])
                a += 1
            if dist(b_x, b_y, BC[i][0], BC[i][1]) <= BC[i][2]:
                bc_b.append(BC[i][3])
                b += 1
    #print(bc_check, a_x, a_y, b_x, b_y, total, a, b)            
    if bc_check:
        if len(bc_check)==1:
            total += bc_check[0]
        else:
            if a==0 or b==0:
                if a==0:
                    total += max(bc_b)
                else:
                    total += max(bc_a)
            else:
                total += max(bc_check)
                idx = 0
                for i in range(len(bc_check)):
                    if bc_check[i] == max(bc_check):
                        idx = i
                bc_check.pop(idx)
                total += max(bc_check)
            
def dist(x_a, y_a, x_b, y_b):
    return abs(x_a-x_b)+abs(y_a-y_b)

dir_ = ((0,0), (0,-1), (1,0), (0,1), (-1, 0))

for test_case in range(1, T+1):
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    BC = []
    total = 0
    for _ in range(A):
        BC.append(tuple(map(int, input().split()))) #x, y, C, P

    BC_c = [False]*A

    t = 0
    stack = [[1,1,10,10]]
    while(t<M):
        a_x, a_y, b_x, b_y = stack.pop()
        #print(t, end=' -> ')
        check(a_x, a_y, b_x, b_y)
        t+= 1
        A_dx, A_dy = dir_[move_A.pop(0)]
        B_dx, B_dy = dir_[move_B.pop(0)]
        nA_x, nA_y = a_x+A_dx, a_y+A_dy
        nB_x, nB_y = b_x+B_dx, b_y+B_dy
        stack.append([nA_x, nA_y, nB_x, nB_y])
    a_x, a_y, b_x, b_y = stack.pop()
    check(a_x, a_y, b_x, b_y)

    print("#{} {}".format(test_case, total))
