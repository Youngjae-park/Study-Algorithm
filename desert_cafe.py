T = int(input())

dir_ = ((1,1),(1,-1),(-1,-1),(-1,1),(1,1)) #오아래, 왼아래, 왼위, 오위

def find(cafe, checked, desert, s_i, s_j, n_i, n_j, dir_c):
    global max_
    #print(desert, (s_i, s_j), (n_i, n_j), dir_c)

    if [s_i, s_j] == [n_i, n_j] and dir_c == 4:
        cnt = len(desert)
        if cnt>max_:
            max_ = cnt
        return


    if dir_c <4 :
        for idx in range(dir_c,dir_c+2):
            di, dj = dir_[idx]
            new_i, new_j = n_i + di, n_j + dj
            if -1<new_i<N and -1<new_j<N:
                if cafe[new_i][new_j] in desert:
                    #print(s_i, s_j, new_i, new_j)
                    if [s_i,s_j] == [new_i,new_j]:
                        #print("here", s_i, s_j, new_i, new_j, dir_c)
                        find(cafe, checked, desert, s_i, s_j, new_i, new_j, dir_c+1)
                    else:
                        continue
                        
                if cafe[new_i][new_j] not in desert:
                    desert.append(cafe[new_i][new_j])
                    checked[new_i][new_j] = True
                    if idx == dir_c:
                        find(cafe, checked, desert, s_i, s_j, new_i, new_j, dir_c)
                    else:
                        find(cafe, checked, desert, s_i, s_j, new_i, new_j, dir_c+1)
                    checked[new_i][new_j] = False
                    desert.pop()

for test_case in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    checked = [[False]*N for _ in range(N)]
    max_ = -1

    for i in range(N):
        for j in range(N):
            checked[i][j] = True
            find(cafe, checked, [cafe[i][j]], i, j, i, j, 0)
            checked[i][j] = False
            
    print("#{} {}".format(test_case, max_))

'''
1
7
7 4 1 5 1 7 9
9 4 6 1 4 6 8
9 6 4 8 4 7 4
3 2 6 2 4 2 8
4 9 4 6 2 4 7
1 7 6 8 9 5 8
1 9 4 7 2 9 7
'''
