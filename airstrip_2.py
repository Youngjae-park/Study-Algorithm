T = int(input())

def masking(arr):
    cnt_RD = 0
    cnt_LD = 0
    check_flat = [False]*N
    check_RD = [False]*N
    check_LD = [False]*N
    for idx in range(len(arr)-1):
        if arr[N-1-idx] == arr[N-1-idx-1]:
            check_flat[N-1-idx] = True
        if arr[idx] == arr[idx+1]:
            check_flat[idx] = True
        #왼쪽이 더 큼
        if arr[idx] == arr[idx+1] + 1:
            cnt_RD = 0
            for di in range(1, X+1):
                if idx + di < N and arr[idx+di]+1 == arr[idx]:
                    cnt_RD += 1
                    if cnt_RD == X:
                        check_RD[idx+1:idx+1+X] = [True]*X
        #오른쪽이 더 큼
        if arr[N-1-idx] == arr[N-1-idx-1] + 1:
            cnt_LD = 0
            for di in range(-1, -X-1, -1):
                if N-1-idx + di >-1 and arr[N-1-idx+di]+1 == arr[N-1-idx]:
                    cnt_LD += 1
                    if cnt_LD == X:
                        check_LD[N-1-idx-X:N-1-idx] = [True]*X

    return check_RD, check_LD

def checking(arr, check_sum):
    check_RD, check_LD = check_sum
    check_LR_RD = []
    for i in range(len(check_RD)):
        if check_RD[i] and check_LD[i]:
            check_LR_RD.append(True)
        else:
            check_LR_RD.append(False)
    #print(check_RD, check_LD)
    #print(check_LR_RD)
    if check_LR_RD.count(True) > 0:
        return False
    else:
        height = arr[0]
        cnt_RD = 0
        cnt_LD = 0
        for i in range(len(arr)):
            #print(height)
            #if arr[i] != height:
            #    return False
            if check_RD[i] == True:
                cnt_RD += 1
                #print("RD")
                if cnt_RD == 1:
                    #print("here")
                    height = height-1
                elif cnt_RD == X:
                    cnt_RD = 0
            if arr[i] != height:
                return False
            if check_LD[i] == True:
                cnt_LD += 1
                if cnt_LD == X:
                    height += 1
                    cnt_LD = 0
            if i == len(arr)-1:
                return True
        
            
    
        
        

for test_case in range(1, T+1):
    N, X = map(int, input().split())
    runway = [[] for _ in range(N)]
    ans = 0

    for i in range(N):
        runway[i] = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if checking(runway[i], masking(runway[i])):
            ans += 1
        temp = []
        for j in range(N):
            temp.append(runway[j][i])
        #print(temp)
        if checking(temp, masking(temp)):
            ans += 1

    #print(checking(runway[2], masking(runway[2])))
    
    print("#{} {}".format(test_case, ans))
    

'''
exlusive or

0 0 0
0 1 1
1 0 1
1 1 0

#평지 or (경사로R exclusive or 경사로L)
'''
    
    
