T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    locker = list(input())
    split_locker = [[] for _ in range(4)]
    for i in range(len(locker)):
        if locker[i] == 'A':
            locker[i] = 10
        elif locker[i] == 'B':
            locker[i] = 11
        elif locker[i] == 'C':
            locker[i] = 12
        elif locker[i] == 'D':
            locker[i] = 13
        elif locker[i] == 'E':
            locker[i] = 14
        elif locker[i] == 'F':
            locker[i] = 15
        else:
            locker[i] = int(locker[i])

    #split
    n = len(locker)//4
    for k in range(4):
        split_locker[k] = locker[n*k:n*(k+1)]

    case = []

    #0회전
    for i in range(4):
        temp = 0
        for j in range(n):
            temp = 16*temp + split_locker[i][j]
        case.append(temp)
    
        
    #1회전 ~ n-1 회전    
    for rot in range(1,n):
        split_locker[1].insert(0,split_locker[0].pop())
        split_locker[2].insert(0,split_locker[1].pop())
        split_locker[3].insert(0,split_locker[2].pop())
        split_locker[0].insert(0,split_locker[3].pop())
        #print(split_locker)
        for i in range(4):
            temp = 0
            for j in range(n):
                temp = 16*temp + split_locker[i][j]
            case.append(temp)
    case = sorted(set(case), reverse = True)
    
    print("#{} {}".format(test_case, case[K-1]))

    
        
        
        

    

    
        

'''input
1
12 10
1B3B3B81F75E
'''
