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
                stem_loc.append([i, j])

    t = 0
    while True:
        t += 1
        tmp = []
        tmp_loc = []
        delete = []

        for i in range(len(stem)):
            if stem[i][3] == 2:
                delete.append(i)
                continue
            elif stem[i][3] == 1:
                if stem[i][4] == 0:
                    for di, dj in (0,1), (0,-1), (1,0), (-1,0):
                        ni = stem[i][0] + di
                        nj = stem[i][1] + dj
                        if [ni, nj] not in stem_loc:
                            if [ni, nj] not in tmp_loc:
                                tmp.append([ni, nj, stem[i][2]])
                                tmp_loc.append([ni, nj])
                            else:
                                for k in range(len(tmp)):
                                    if tmp[k][0] == ni and tmp[k][1] == nj:
                                        tmp[k] = [ni, nj, max(stem[i][2], tmp[k][2])]
                                        break
                stem[i][4] += 1
                if stem[i][4] == stem[i][2]:
                    stem[i][3] = 2
            elif stem[i][3] == 0:
                stem[i][4] += 1
                if stem[i][4] == stem[i][2]:
                    stem[i][3] = 1
                    stem[i][4] = 0
        for i in range(len(tmp)):
            t_i, t_j, t_size = tmp.pop()
            stem.append([t_i, t_j, t_size, 0, 0])
            stem_loc.append([t_i, t_j])

        if t == K:
            break

    cnt = 0
    for x in stem:
        if x[3] == 0 or x[3] == 1:
            cnt += 1

    print("#{} {}".format(test_case, cnt))
