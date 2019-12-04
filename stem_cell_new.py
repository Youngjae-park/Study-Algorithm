T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    grid = [[False for _ in range(M+2*K)] for __ in range(N+2*K)]
    cells = []
    alive = 0
    
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cells.append([i+K,j+K,arr[i][j],arr[i][j],arr[i][j]]) #x, y, size, time, life
                grid[i+K][j+K] = True
                alive += 1

    
    cells = sorted(cells, key = lambda x : x[2], reverse= True)
    for t in range(K):
        for x in range(len(cells)):
            #print("now : ", cells[0])
            i, j, size, time, life = cells.pop(0)
            grid[i][j] = True
            if time>0:
                time -= 1
                cells.append([i, j, size, time, life])
            elif time == 0:
                life -= 1
                for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
                    ni = i + di
                    nj = j + dj
                    if not grid[ni][nj]:
                        grid[ni][nj] = True
                        cells.append([ni, nj, size, size, size])
                        alive += 1
                if life == 0:
                    time = -1
                    alive -= 1
                else:
                    cells.append([i, j, size, time, life])
        
        #print(t+1, "->" , "sum : ", len(cells),"\n" ,cells)

    print("#{} {}".format(test_case, alive))
                        
            
                
            
'''input
1
2 2 10
1 1
0 2
'''
