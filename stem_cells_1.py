T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(N)]
    stem = []
    stem_loc = []
    for i in range(N):
        for j in range(M):
            if map_[i][j]:
                stem.append([i, j, map_[i][j], 0, 0])
                stem_loc.append([i,j])
    t = 0
    while True:
        t += 1
        tmp = []
        tmp_loc = dict()
        delete = []
        
        for i in range(len(stem)):
            if stem[i][3] == 2:
                delete.append(i)
                continue
            elif stem[i][3] == 1:
                if stem[i][4] == 0:
                    for di, dj in (0,1),(0,-1),(1,0),(-1,0):
                        ni = stem[i][0] + di
                        nj = stem[i][1] + dj
                        if [ni, nj] not in stem_loc:
                            if (ni, nj) not in tmp_loc.keys():
                                tmp_loc[ni, nj] = stem[i][2]
                            else:
                                tmp_loc[ni, nj] = max(tmp_loc[ni, nj], stem[i][2])
                stem[i][4] += 1
                if stem[i][4] == stem[i][2]:
                    stem[i][3] = 2
            elif stem[i][3] == 0:
                stem[i][4] += 1
                if stem[i][4] == stem[i][2]:
                    stem[i][3] = 1
                    stem[i][4] = 0
        
        '''
        count = 0
        for i in range(len(delete)):
            stem.pop(delete[i]-count)
            count += 1
        '''
        
        for i in tmp_loc.keys():
            t_i, t_j = i
            stem.append([t_i, t_j, tmp_loc[i], 0, 0])
            stem_loc.append([t_i, t_j])
        

        #print("time : ", t)
        #print(stem)
        #print(tmp)
        #print(tmp_loc)
        
        if t == K:
            break

    cnt = 0
    for x in stem:
        if x[3] == 0 or x[3] == 1:
            cnt += 1
    
    print("#{} {}".format(test_case, cnt))
                
