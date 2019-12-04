T = int(input())

def check(arr_film, num_K):
    for j in range(W):
        c_cnt = 1
        past = arr_film[0][j]
        for i in range(1,D):
            if past == arr_film[i][j]:
                c_cnt += 1
                if cnt +1 > num_K:
                    break
            else:
                cnt = 1
            past = arr_film[i][j]
        if cnt +1 > num_K:
            continue
        else:
            return False
    return True

for test_case in range(1, T+1):
    D, W, K = map(int, input().split())
    origin_film = [list(map(int, input().split())) for _ in range(D)]
    origin_depth = [0]*D
    origin_choose = [False]*D
    min_ = 999999
    queue = [[0,origin_depth,origin_choose,origin_film, 0]] #cnt 갯수, depth, choose, film

    while queue:
        cnt, depth, choose, film, idx = queue.pop(0)
        if check(film, K):
            min_ = min(min_, cnt)
            break
        else:
            cnt += 1
            for i in range(idx, D):
                if not choose[i]:
                    choose[i] = True
                    depth[i] = 1
                    film[i] = [0]*W
                    
                    
