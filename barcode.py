T = int(input())

bar = [[0,0,0,1,1,0,1], [0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

def check(code):
    sum_ = 0
    for i in range(0,8,2):
        sum_ += code[i]
    sum_ = sum_*3
    for i in range(1,8,2):
        sum_ += code[i]
    if sum_ % 10 == 0:
        return True
    else:
        return False
    

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    barcode = list(list(map(int, input())) for _ in range(N))
    s_i = 0
    s_j = 0
    remember = []

    flag_= False
    for i in range(N):
        for j in range(M):
            if barcode[i][j] != 0:
                s_i = i
                s_j = j
                flag_ = True
                if flag_:
                    break
        if flag_:
            break
                
    left = 0
    flag = False
    for cnt in range(7):
        if s_j-cnt>-1:
            for x in range(10):
                if barcode[s_i][s_j-cnt:s_j-cnt+7] == bar[x]:
                    flag = True
                    left = cnt
                    break
            if flag: break

    s_i = i
    s_j = s_j - left
    cnt = 0
    #print(s_i, s_j)
    flag = 0
    for s in range(8):
        for x in range(10):
            if barcode[s_i][s_j+s*7:s_j+(s+1)*7] == bar[x]:
                remember.append(x)
                if len(remember) == 8:
                    flag = 1
                break
            else:
                if len(remember) == 8:
                    flag = 1
                else:
                    if x == 9:
                        flag = 2
            if flag != 0:
                break
        if flag != 0:
            break
                
    if len(remember) == 8:
        if check(remember):
            print("#{} {}".format(test_case, sum(remember)))
        else:
            print("#{} 0".format(test_case))
        continue
    
    if flag == 2:
        print("#{} 0".format(test_case))
    elif flag == 1:
        print("#{} {}".format(test_case, sum(remember)))
