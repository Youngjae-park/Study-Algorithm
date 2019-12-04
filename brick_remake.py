T = int(input())

def sol(n, arr, cnt):
    global min_
    if n == N or not cnt:
        min_ = min(min_, cnt)
        return
    else:
        for j in range(W):
            q = []
            for i in range(H):
                new_brick = [x[:] for x in arr]
                if new_brick[i][j]:
                    new_count = cnt - 1
                    q.append((i,j,new_brick[i][j]))
                    new_brick[i][j] = 0
                    break
            if not q:
                continue
            while q:
                i, j, length = q.pop()
                for k in range(1, length):
                    for di, dj in (0,-1),(0,1),(-1,0),(1,0):
                        ni = i + k*di
                        nj = j + k*dj
                        if -1<ni<H and -1<nj<W and new_brick[ni][nj]:
                            if new_brick[ni][nj]>1:
                                q.append((ni,nj,new_brick[ni][nj]))
                            new_brick[ni][nj] = 0
                            new_count -= 1
            for j in range(W):
                bottom = H-1
                for i in range(H-1, -1, -1):
                    if new_brick[i][j]:
                        new_brick[bottom][j], new_brick[i][j] = new_brick[i][j], new_brick[bottom][j]
                        bottom -= 1
                        
            sol(n+1, new_brick, new_count)
                
                            
                
    
    
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    count = sum(1 for a in brick for b in a if b)

    min_ = 9999

    sol(0, brick, count)

    print("#{} {}".format(test_case, min_))
    
