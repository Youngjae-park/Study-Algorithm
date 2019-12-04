import itertools
import copy

T = int(input())

def clear(brick):
    for j in range(W):
        tmp = []
        for i in range(H):
            tmp.append(brick[i][j])
        #go_up
        for idx in range(H):
            if tmp[idx][1]:
                tmp[idx][0] = 0
                tmp[idx][1] = False
                tmp.insert(0,tmp.pop(idx))
        for i in range(H):
            brick[i][j] = tmp[i]

def break_(brick, col):
    checked = [[False for _ in range(W)] for _ in range(H)]
    start_i = H-1
    for i in range(H):
        if brick[i][col][0] != 0 and brick[i][col][1] == 0:
            start_i = i
            break
    
    queue = []
    queue.append((start_i, col, brick[start_i][col][0], brick[start_i][col][1]))
    checked[start_i][col] = True
    while queue:
        queue = list(set(queue))
        i, j, length, state = queue.pop(0)
        checked[i][j] = True
        if length > 1 and not state :
            for dif in range(1, length):
                if i + dif < H and not checked[i+dif][j]:
                    queue.append((i+dif, j, brick[i+dif][j][0], brick[i+dif][j][1]))
                    checked[i+dif][j] = True
                if i - dif > -1 and not checked[i-dif][j]:
                    queue.append((i-dif, j, brick[i-dif][j][0], brick[i-dif][j][1]))
                    checked[i-dif][j] = True
                if j + dif < W and not checked[i][j+dif]:
                    queue.append((i, j+dif, brick[i][j+dif][0], brick[i][j+dif][1]))
                    checked[i][j+dif] = True
                if j - dif > -1 and not checked[i][j-dif]:
                    queue.append((i, j-dif, brick[i][j-dif][0], brick[i][j-dif][1]))
                    checked[i][j-dif] = True
        #print(len(queue))

        brick[i][j][1] = True
    clear(brick)

def count_brick(brick):
    global min_
    cnt = 0
    for i in range(H):
        for j in range(W):
            if brick[i][j][0] != 0:
                cnt += 1
    if cnt < min_:
        min_ = cnt
    
            

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [[] for _ in range(H)]
    min_ = W*H

    #initialize brick
    for i in range(H):
        brick[i] = list(map(int, input().split()))

    #initialize brick
    for i in range(H):
        for j in range(W):
            brick[i][j] = [brick[i][j], False]

    num = [i for i in range(W)]
    num = itertools.product(num, repeat=N)
    
    #ct = 0
    for prd in num:
        brick_cp = copy.deepcopy(brick)
        for idx in range(N):
            break_(brick_cp, prd[idx])
            count_brick(brick_cp)
            if min_ == 0:
                break

    print("#{} {}".format(test_case, min_))
    
    
    

    

    
