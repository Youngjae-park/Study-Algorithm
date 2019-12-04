T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    house = [list(map(int, input().split())) for _ in range(N)]
    max_house = sum(M for a in house for b in a if b)
    max_K = 0
    #max_K 정하기
    for k in range(1,N+1):
        if k**2 + (k-1)**2 < max_house:
            max_K = k
        else:
            break

    info_house = []
        
    for i in range(N):
        for j in range(N):
            if house[i][j]:
                info_house.append((i,j))

    max_ = 0
    for i in range(N):
        for j in range(N):
            for k in range(1, max_K+2):
                cnt = 0
                for t_i in range(i-(k-1),i+(k-1)+1):
                    for t_j in range(j-(k-1), j+(k-1)+1):
                        if -1<t_i<N and -1<t_j<N:
                            if abs(t_i-i)+abs(t_j-j)<k:
                                if (t_i,t_j) in info_house:
                                    cnt += 1
                if cnt*M >= k**2+(k-1)**2:
                    if max_ < cnt:
                        max_ = cnt

    print("#{} {}".format(test_case, max_))
                                
                
