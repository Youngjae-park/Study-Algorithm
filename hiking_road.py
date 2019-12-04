T = int(input())

def find(i,j, now, cnt, flag, checked):
    global max_
    #print(i,j,now,cnt,flag)
    if cnt>max_:
        max_ = cnt

    #flag 가 True 이면 산을 이미 한번 깍은 상태
    if flag:
        for di, dj in (0,1),(1,0),(0,-1),(-1,0):
            ni = i + di
            nj = j + dj
            if -1<ni<N and -1<nj<N:
                if map_[ni][nj] < now and not checked[ni][nj]:
                    checked[ni][nj] = True
                    find(ni, nj, map_[ni][nj], cnt+1, flag, checked)
                    checked[ni][nj] = False

    #flag 가 False 이면 산을 아직 한번도 깍지 않은 상태
    else:
        for di, dj in (0,1),(1,0),(0,-1),(-1,0):
            ni = i + di
            nj = j + dj
            if -1<ni<N and -1<nj<N:
                #산을 깍지 않아도 탐색이 가능한 경우
                if map_[ni][nj] < now and not checked[ni][nj]:
                    checked[ni][nj] = True
                    find(ni, nj, map_[ni][nj], cnt+1, flag, checked)
                    checked[ni][nj] = False
                #산을 깍아야 탐색이 계속 진행 가능한 경우
                elif map_[ni][nj] > now - 1 and not checked[ni][nj]:
                    checked[ni][nj] = True
                    for dk in range(1, K+1):
                        if map_[ni][nj] - dk < now:
                            find(ni,nj, map_[ni][nj]-dk,cnt+1,True, checked)
                            break
                    checked[ni][nj] = False
                    
                    
                

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(N)]
    starting_point = []
    check = [[False for __ in range(N)] for _ in range(N)]
    max_ = 0
    highest = max(max(x) for x in map_)
    
    for i in range(N):
        for j in range(N):
            if map_[i][j] == highest:
                starting_point.append([i, j])

    t= 0
    while starting_point:
        t+=1
        #print("#",t)
        
        s_i, s_j = starting_point.pop(0)
        check[s_i][s_j] = True
        find(s_i,s_j,map_[s_i][s_j],1,False,check)
        check[s_i][s_j] = False

    print("#{} {}".format(test_case, max_))
