T = int(input())

class position():
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

def BFS(x, y, dist):
    global result
    queue.append(position(x, y, dist))
    visited[x][y] = True

    while queue:
        current = queue.pop(0)

        if current.x == end[0] and current.y == end[1]:
            result = current.dist-1
            break

        for dx, dy in dir_:
            next_x = current.x + dx
            next_y = current.y + dy
            next_dist = current.dist + 1

            if -1<next_x<N and -1<next_y<N:
                if visited[next_x][next_y] == False and (maze[next_x][next_y] == 0 or maze[next_x][next_y]==3):
                    visited[next_x][next_y] = True
                    queue.append(position(next_x,next_y,next_dist))

        for a in queue:
            print(a.x, a.y, a.dist, end=' / ')

        print()
                    
                    
        
dir_ = ((0,-1),(-1,0),(0,1),(1,0))    

for test_case in range(1, T+1):
    N = int(input())
    maze = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    result = 0
    queue = []

    for i in range(N):
        maze[i] = list(map(int,input()))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                end = (i, j)
            if maze[i][j] == 2:
                start = (i, j)

    BFS(start[0], start[1], 0)
    print("#{} {}".format(test_case, result))
