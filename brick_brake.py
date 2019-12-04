import itertools
import copy

T = int(input())

class state():
    def __init__(self, i, j, size, state):
        self.i = i
        self.j = j
        self.size = size
        self.state = state

def to_top(j):
    global real_brick
    #find top_idx
    top_idx = 0
    non_zero = []
    for x in range(H):
        if real_brick[x][j].size != 0:
            non_zero.append(real_brick[x][j].size)
    #print(non_zero) 폭발직전 블럭 0이 아닌 블럭 순서
    for x in range(H):
        real_brick[x][j].size = 0
    for x in range(len(non_zero)):
        real_brick[-1-x][j].size = non_zero.pop()

def brick_brake(idx):
    global real_brick
    top_idx = H-1
    #find top_idx
    for i in range(H):
        if real_brick[i][idx].size != 0:
            top_idx = i
            break

    flag = 0
    for i in range(H):
        for j in range(W):
            if real_brick[i][j].size != 0:
                flag += 1
                break
        if flag != 0:
            break

    if flag == 0:
        return
    
    ###real_brick[top_idx][idx].state = True
    stack.append(real_brick[top_idx][idx])

    #탐색 
    while stack:
        ''' stack 정보확인
        for x in stack:
            print(x.i, x.j, x.size, x.state, end=' / ')
        print()
        '''
        #print("len(stack) =>", len(stack))
        target = stack.pop(0)
        real_brick[top_idx][idx].state = True
        for i in range(target.size):
            for di, dj in dir_[i]:
                ni = target.i + di
                nj = target.j + dj
                if -1<ni<H and -1<nj<W:
                    if real_brick[ni][nj].state == False:
                        real_brick[ni][nj].state = True
                        stack.append(real_brick[ni][nj])
    for i in range(H):
        for j in range(W):
            if real_brick[i][j].state:
                if real_brick[i][j].size != 0:
                    real_brick[i][j].size = 0
            real_brick[i][j].state = False
    for j in range(W):
        to_top(j)
                

    
dir_ = [[(0,0)]]
for i in range(1,9):
    temp = [(-i,0),(0,i),(i,0),(0,-i)]
    dir_.append(temp)

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [[0]*W for _ in range(H)]
    real_brick = [[0]*W for _ in range(H)]
    checked = [[False]*W for _ in range(H)]
    stack = []

    #가능한 가짓 수 만들기
    width = []
    for i in range(W):
        width.append(i)
    num_width = itertools.product(width, repeat=N)
    ''' 중복순열 확인하기
    for x in num_width:
        print(x)
    '''
    for i in range(H):
        brick[i] = list(map(int,input().split()))

    for i in range(H):
        for j in range(W):
            real_brick[i][j] = state(i, j, brick[i][j], False)

    '''
    test = (2,2,6)
    for x in range(N):
        print("# ", x)
        brick_brake(test[x])
        for i in range(H):
            for x in real_brick[i]:
                print("[", x.i, x.j, x.size, x.state, "]", end=' ')
            print()
        print()
    '''    
        
    
    real_brick_temp = copy.deepcopy(real_brick)
    
    sum_rest = []
    #N번 반복하기
    for x in num_width:
        #print(x)
        rest = 0
        for i in range(N):
            brick_brake(x[i])
        #count 하기
        for i in range(H):
            for j in range(W):
                if real_brick[i][j].size != 0:
                    rest += 1
        real_brick = copy.deepcopy(real_brick_temp)
        sum_rest.append(rest)

    print("#{} {}".format(test_case, min(sum_rest)))
    
    
    '''
    #눈에 보이게 하기
    for i in range(H):
        for x in real_brick[i]:
            print("[", x.i, x.j, x.size, x.state, "]", end=' ')
        print()
    '''
