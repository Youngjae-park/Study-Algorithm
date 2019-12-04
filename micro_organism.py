T = int(input())

dir_ = [[],[-1,0],[1,0],[0,-1],[0,1]]

def rest():
    pass

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    association = []
    for _ in range(K):
        association.append(list(map(int, input().split())))
    map_ = [[False for _ in range(N)] for __ in range(N)]

    #테두리
    for i in range(N):
        for j in range(N):
            if i==0 or j == 0 or i == N-1 or j == N-1:
                map_[i][j] = True

    #시간 반복
    for t in range(1, M+1):
        #이동
        for _ in range(len(association)):
            t_i, t_j, amount, dir_c = association.pop(0)
            di, dj = dir_[dir_c]
            ni, nj = t_i + di, t_j + dj
            if -1<ni<N and -1<nj<N:
                if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
                    if dir_c == 1:
                        dir_c = 2
                    elif dir_c == 2:
                        dir_c = 1
                    elif dir_c == 3:
                        dir_c = 4
                    elif dir_c == 4:
                        dir_c = 3
                    amount = int(amount/2)
                    if amount:
                        association.append([ni, nj, amount, dir_c])
                else:
                    association.append([ni, nj, amount, dir_c])

        
        #겹치는 위치 체크
        ssang = [[0 for _ in range(N)] for __ in range(N)]
        #count 겹치는 개수
        for i in range(len(association)):
            ssang[association[i][0]][association[i][1]] += 1

        #print(ssang)
        for i in range(N):
            for j in range(N):
                if ssang[i][j] > 1:
                    amount = []
                    dir_next = []
                    cnt = 0
                    for x in range(len(association)):
                        if [association[x-cnt][0], association[x-cnt][1]] == [i, j]:
                            #print(len(association), association)
                            amount.append(association[x-cnt][2])
                            dir_next.append(association[x-cnt][3])
                            association.pop(x-cnt)
                            cnt+=1
                            
                    max_ = 0
                    max_i = 0
                    for k in range(len(amount)):
                        if max_ < amount[k]:
                            max_ = amount[k]
                            max_i = k
                    #print(i, j, " ", dir_next, amount, max_i)
                    association.append([i,j,sum(amount),dir_next[max_i]])
        #print(t)
        #for x in association:
        #    print(x)

    total_sum = sum(x[2] for x in association)

    print("#{} {}".format(test_case, total_sum))
