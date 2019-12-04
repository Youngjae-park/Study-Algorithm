T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    start_i, start_j = (0,0)
    goal_i, goal_j = (0,0)
    maze = []
    stack = []
    visited = list([False]*N for _ in range(N))
    flag = True
    for _ in range(N):
        maze.append(list(input()))
    
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_i, start_j = (i,j)
            if maze[i][j] == '3':
                goal_i, goal_j = (i,j)

    stack.append((start_i, start_j))
    visited[start_i][start_j] = True
    while(flag):
        #print(stack)
        if(len(stack) == 0):
            print("#{0} 0".format(test_case))
            break
        pos_i, pos_j = stack.pop()
        visited[pos_i][pos_j] = True
        for dx, dy in [(0,-1),(-1,0),(0,1),(1,0)]:
            pos_ix = pos_i + dx
            pos_jx = pos_j + dy
            if(-1<pos_ix<N and -1<pos_jx<N):
                if(maze[pos_ix][pos_jx]=='0' and visited[pos_ix][pos_jx]==False):
                    stack.append((pos_ix,pos_jx))
                    #visited[pos_i][pos_j]==True
                elif(maze[pos_ix][pos_jx]=='3'):
                    print("#{0} 1".format(test_case))
                    flag = False
                    break
                
