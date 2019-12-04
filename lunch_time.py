T = int(input())

def dist_(i, j, k):
    if k:
        return abs(i-stair[0][0])+abs(j-stair[0][1])
    else:
        return abs(i-stair[1][0])+abs(j-stair[1][1])

def count_t(s_A, s_B):
    global min_
    t = 1
    wait_A = [0]*3
    wait_B = [0]*3
    
    while (s_A or s_B) or not (wait_A.count(0)==3 and wait_B.count(0)==3):
        #print(t, s_A, s_B, wait_A, wait_B)
        if t> min_:
            t += 1
            break

        
        for i in range(3):
            if wait_A[i] != 0:
                wait_A[i] += 1
                if wait_A[i] == floor[stair[0][0]][stair[0][1]]+1:
                    wait_A[i] = 0
            if wait_B[i] != 0:
                wait_B[i] += 1
                if wait_B[i] == floor[stair[1][0]][stair[1][1]]+1:
                    wait_B[i] = 0
                
        if s_A:
            k = s_A.count(s_A[-1])
            if s_A[-1] < t+1:
                for _ in range(k):
                    for i in range(3):
                        if wait_A[i] == 0:
                            s_A.pop()
                            wait_A[i] = 1
                            break
                        
        if s_B:
            k = s_B.count(s_B[-1])
            if s_B[-1] < t+1:
                for _ in range(k):
                    for i in range(0,3):
                        if wait_B[i] == 0:
                            s_B.pop()
                            wait_B[i] = 1
                            break

        #print(t, s_A, s_B, wait_A, wait_B)

        t += 1

    if t<min_:
        min_ = t

def devide(people, A, B, idx):
    if idx == len(people):
        #print("here")
        #print(A,B)
        A = sorted(A, reverse = True)
        B = sorted(B, reverse = True)
        count_t(A, B)
        return
        
    A.append(people[idx][2])
    devide(people, A, B, idx+1)
    A.pop()
    B.append(people[idx][3])
    devide(people, A, B, idx+1)
    B.pop()
        
        
    
    

for test_case in range(1, T+1):
    N = int(input())
    floor = [list(map(int, input().split())) for _ in range(N)]
    stair = []
    people = []
    min_ = 999999

    for i in range(N):
        for j in range(N):
            if floor[i][j] > 1:
                stair.append((i,j))
            if floor[i][j] == 1:
                people.append([i,j])

    for _ in range(len(people)):
        p_i, p_j = people.pop(0)
        people.append([p_i, p_j, dist_(p_i,p_j,1), dist_(p_i,p_j,0)])

    devide(people, [], [], 0)

    print("#{} {}".format(test_case, min_))

'''
1->도착
2->1 1 1
3->2 2 2
4->1 0 0
5->2 0 0
'''



    
