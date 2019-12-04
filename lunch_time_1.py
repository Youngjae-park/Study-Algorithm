T = int(input())

def dist(s_i, s_j, g_i, g_j):
    return abs(s_i-g_i)+abs(s_j-g_j)


def solve(wait_A, wait_B, state_A, state_B):
    global min_
    t = 0
    while wait_A or wait_B or state_A.count(0) != 3 or state_B.count(0) != 3:
        if t>min_:
            t += 1
            break

        for i in range(3):
            if state_A[i] !=0:
                state_A[i] += 1
                if state_A[i] == stair[0][2]+1:
                    state_A[i] = 0
            if state_B[i] !=0:
                state_B[i] += 1
                if state_B[i] == stair[1][2]+1:
                    state_B[i] = 0
            
        if wait_A:
            for _ in range(3):
                if wait_A:
                    if wait_A[-1] < t+2:
                        for i in range(3):
                            if state_A[i] == 0:
                                state_A[i] = 1
                                wait_A.pop()
                                break
                else:
                    break
        if wait_B:
            for _ in range(3):
                if wait_B:
                    if wait_B[-1] < t+2:
                        for i in range(3):
                            if state_B[i] == 0:
                                state_B[i] = 1
                                wait_B.pop()
                                break
                else:
                    break

        t += 1

    if t<min_:
        min_ = t+1

        
def make(choice, k):
    if k == len(choice):
        wait_A = []
        wait_B = []
        for i in range(len(choice)):
            if not choice[i]:
                wait_A.append(people[i][0])
            else:
                wait_B.append(people[i][1])
        wait_A_ = sorted(wait_A, reverse = True)
        wait_B_ = sorted(wait_B, reverse = True)
        solve(wait_A_, wait_B_, [0,0,0], [0,0,0])

        #여기에 새로운 함수 넣기 input wait_A, wait_B
        
        return
    else:
        make(choice, k+1)
        choice[k] =1
        make(choice, k+1)
        choice[k] =0
                
        

for test_case in range(1, T+1):
    N = int(input())
    floor = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stair = []
    min_ = 999999
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if floor[i][j] == 1:
                people.append([i,j])
            if floor[i][j] > 1 :
                stair.append([i,j,floor[i][j]])

    for i in range(len(people)):
        people[i] = [dist(people[i][0], people[i][1], stair[0][0], stair[0][1]), dist(people[i][0], people[i][1], stair[1][0], stair[1][1])]

    choice_ = [0]*len(people)
    make(choice_, 0)

    print("#{} {}".format(test_case, min_))
    
