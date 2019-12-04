T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(N)]
    stem = dict()

    for i in range(N):
        for j in range(M):
            if map_[i][j]:
                stem[i, j] = [map_[i][j], 0, 0]

    t = 0
    while True:
        t += 1
        tmp = stem.keys()       
        print(tmp)
        for x in tmp:
            i, j = x
            if stem[i, j][1] == 2:
                continue
            elif stem[i, j][1] == 1:
                if stem[i, j][2] == 0:
                     for di, dj in (0,1),(0,-1),(1,0),(-1,0):
                        ni = i + di
                        nj = j + dj
                        if (ni, nj) not in stem.keys():
                            stem[ni, nj] = [stem[i, j][0], 0, 0]
                        else:
                             if stem[ni, nj][1] == 0 and stem[ni, nj][2] == 0:
                                stem[ni, nj][0] = max(stem[i, j][0], stem[ni, nj][0])
                stem[i, j][2] += 1
                if stem[i, j][2] == stem[i, j][0]:
                    stem[i, j][1] = 2
            elif stem[i, j][1] == 0:
                stem[i, j][2] += 1
                if stem[i,j][2] == stem[i, j][0]:
                    stem[i,j][1] = 1
                    stem[i,j][2] = 0

        if t == K:
            break

    cnt = 0
    for x in stem:
        if x[1] == 0 or x[1] == 1:
            cnt += 1

    print("#{} {}".format(test_case, cnt))
