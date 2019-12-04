import itertools,copy
dx=[0,1,0,-1]
dy=[-1,0,1,0]
def IS(y,x):
    if -1<y<L[2] and -1<x<L[1]:return True
    return False
def DFS(y,x,c):
    M[y][x]=0
    for dir in range(4):
        h=1
        while h!=c:
            nY=y+h*dy[dir]
            nX=x+h*dx[dir]
            if not IS(nY,nX):break
            if M[nY][nX]:
                DFS(nY,nX,M[nY][nX])
            h+=1
def down():
    for x in range(L[1]):
        for y in range(L[2]-1,0,-1):
            n=y-1
            if not M[y][x]:
                while n>=0:
                    if M[n][x]:
                        M[y][x]=M[n][x]
                        M[n][x]=0
                        break
                    n-=1
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    A=[[int(x)for x in input().split()]for y in range(L[2])]
    C=[int(_)for _ in range(L[1])]
    R=1000
    comb=list(itertools.product(C,repeat=L[0]))
    for c in comb:
        M=copy.deepcopy(A)
        r=0
        for i in c:
            for j in range(L[2]):
                if M[j][i]:
                    DFS(j,i,M[j][i])
                    down()
                    break
        for k in range(L[2]):
            for l in range(L[1]):
                if M[k][l]:r+=1
        if r<R:R=r
    print('#%d %d'%(n+1,R))
