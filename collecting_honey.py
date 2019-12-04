import itertools

T = int(input())



def cal_benefit(arr,visited,C,cnt,i,j):
    global sum_
    per_arr = itertools.permutations(arr)
    
    temp = []
    
    for c_per_arr in per_arr:
        #print(c_per_arr)
        cnt = 0
        cnt_p = 0
        for elem in c_per_arr:
            if cnt + elem <= C:
                cnt_p = cnt_p + elem**2
                cnt = cnt + elem
            else:
                break
        temp.append(cnt_p)
    sum_[i].append(max(temp))
    '''
    sum_arr = 0

    while arr:
        max_honey = max(arr)
        if cnt + max_honey <=C:
            temp.append(max_honey)
            arr.remove(max_honey)
            cnt = cnt + max_honey
        else:
            arr.remove(max_honey)
    '''
    '''
    
    for a in temp:
        sum_arr = sum_arr + a**2
    sum_[i][j] = (sum_arr)
    '''        
        
    

def collecting(N,M,C):
    for i in range(N):
        for j in range(N-M+1):
            c_honey = honey[i][j:j+M]
            #print(c_honey)
            cal_benefit(c_honey, visited, C, 0,i,j)
            
    

for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    result = 0
    sum_ = [[] for _ in range(N)]
    visited = [False]*M

    #initialize honeybox
    honey = [[0]*N]*N
    for i in range(N):
        honey[i] = list(map(int,input().split()))

    
    collecting(N,M,C)
    max_sum = []
    for arr in sum_:
        max_sum.append(max(arr))

    max1 = max(max_sum)
    max_sum.remove(max1)
    max2 = max(max_sum)

    print("#{} {}".format(test_case, max1+max2))
        
    










'''
input ex)
1
4 2 13
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7
'''
