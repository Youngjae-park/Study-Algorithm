T = int(input())

class stem_cell():
    def __init__(self, i, j, X, cnt, state):
        self.i = i
        self.j = j
        self.X = X
        self.cnt = cnt
        self.state = state
        #state 죽은 상태 2 활성 상태 1 비활성 상태 0

def expand():
    global grid
    grid.insert(0,[0]*(len(grid[0])+2))
    for i in range(1,len(grid)):
        grid[i].insert(0,0)
        grid[i].append(0)
    grid.append([0]*len(grid[0]))

def grow(cell):
    if cell.cnt == cell.X and cell.state == 0:
        cell.state = 1
        cell.cnt = 0
    if cell.cnt == cel.X and cell.state == 1:
        cell.state = 2
        for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
            if grid[cell.i+

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    grid = [[] for _ in range(N)]
    for i in range(N):
        grid[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(M):
            grid[i][j] = stem_cell(i,j,grid[i][j],0,0)

    

    
    
    




'''input
1
2 2 10
1 1
0 2
'''
