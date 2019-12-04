N = int(input())

sea_visited = list([False]*N for _ in range(N))
sea = []
pos_x, pos_y = (0,0)
for _ in range(N):
    sea.append(list(input().split()))
for i in range(N):
    for j in range(N):
        if(sea[i][j] == '9'):
            sea_visited[i][j] = True
            pos_x, pos_y = (i,j)
