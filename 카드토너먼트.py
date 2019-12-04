T = int(input())

def DIVIDE(arr):
    global ton_divided
    if(len(arr)<=2):
        ton_divided.append(tuple(arr))
        return
    if(len(arr)%2==0):
        L_length = len(arr)//2
    else:
        L_length = len(arr)//2 + 1
    R_length = len(arr)-L_length
    L_arr = arr[:L_length]
    R_arr = arr[L_length:]
    DIVIDE(L_arr)
    DIVIDE(R_arr)

def RPS(ton_divided):
    global ton
    global test_case
    if(len(ton_divided)==1 and len(ton_divided[0]) == 1):
        answer = ton_divided[0][0]
        print("#{} {}".format(test_case, answer))
        return
    for _ in range(len(idx_N)):            
        if(len(ton_divided[0])==1):
            l_arr = idx_N.pop(0)
            ton_divided.append(l_arr)
        else:
            l_arr, r_arr = ton_divided.pop(0)
            if(ton[l_arr]==ton[r_arr]):
                ton_dividied.append(l_arr)
            elif(ton[l_arr]+1==ton[r_arr] or ton[r_arr]+2==ton[l_arr]):
                ton_divided.append(r_arr)
            else:
                ton_divided.append(l_arr)
        
    
for test_case in range(1, T+1):
    N = int(input())
    ton = list(map(int,input().split()))
    flag = [True]*N
    ton_divided = []
    idx_N = [i for i in range(N)]
    DIVIDE(idx_N)
    while(len(ton_divided)!=1):
        print(ton_divided)
        RPS(ton_divided)
        DIVIDE(ton_divided)
