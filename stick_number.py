T = int(input())

def find(i,j,num,cnt):
    global stack
    #print(i, j, num, cnt)
    if cnt == 7:
        tot = 0
        for i in range(7):
            tot = tot*10 + num[i]
        if tot not in stack:
            stack.append(tot)
            
                
    else:
        for idx in range(4):
            di, dj = dir_[idx]
            ni = i + di
            nj = j + dj
            if -1<ni<4 and -1<nj<4:
                num.append(grid[ni][nj])
                find(ni,nj,num,cnt+1)
                num.pop()
                

dir_ = ((-1,0),(0,1),(1,0),(0,-1))

for test_case in range(1, T+1):
    grid = list(list(map(int, input().split())) for _ in range(4))
    stack = []

    temp = []
    
    for i in range(4):
        for j in range(4):
            temp.append([i,j])

    while(temp):
        i, j = temp.pop()
        find(i,j,[grid[i][j]],1)

    print("#{} {}".format(test_case, len(stack)))
