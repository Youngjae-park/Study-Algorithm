T = int(input())

def check(arr_film, num_K):
    for j in range(W):
        cnt = 1
        past = arr_film[0][j]
        for i in range(1,D):
            if past == arr_film[i][j]:
                cnt += 1
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

def print_info(t_film, cnt, depth):
    print(t_film)
    print("#", cnt, depth, min_)

def find(t_film, cnt, depth,idx):
    #print(t_film)
    #print("#", cnt, depth)
    if idx > len(depth):
        return
    global min_
    if cnt>=min_:
        return
    else:
        for i in range(idx, len(depth)):
            #그냥
            
            tmp = []
            for j in range(W):
                tmp.append(t_film[i][j])
            if cnt == 0:    
                depth[i] = 0
                if check(t_film, K):
                    #print("HERE")
                    #print_info(t_film, cnt, depth)
                    min_ = min(min_, cnt)
                else:
                    find(t_film, cnt, depth, i+1)
            #A약
            depth[i] = 1
            t_film[i] = [0]*W
            if check(t_film, K):
                #print_info(t_film, cnt, depth)
                min_ = min(min_, cnt+1)
            else:
                find(t_film, cnt+1, depth, i+1)
            t_film[i] = tmp
            #B약
            depth[i] = 2
            t_film[i] = [1]*W
            if check(t_film, K):
                #print_info(t_film, cnt, depth)
                min_ = min(min_, cnt+1)
            else:
                find(t_film, cnt+1, depth, i+1)
            depth[i] = 0
            t_film[i] = tmp
                

for test_case in range(1, T+1):
    D, W, K = map(int, input().split())
    film =[list(map(int, input().split())) for _ in range(D)]
    depth_F = [0]*D
    min_ = 99999

    find(film, 0, depth_F, 0)

    print("#{} {}".format(test_case, min_))
