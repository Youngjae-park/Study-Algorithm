ewsn=[[0,0,1],[1,0,-1],[2,1,0],[3,-1,0]]
direction=[0,[1,3,0,2],[1,2,3,0],[2,0,3,1],[3,0,1,2],[1,0,3,2]]
  
for tc in range(int(input())):
    N=int(input())
    mat=[]
    warmhole=[[] for _ in range(11)]
    
    for row in range(N+2):
        if row==0 or row==N+1:mat.append([5]*(N+2));continue
        tmp=list(map(int,input().split()))
        tmp.insert(0,5)
        tmp.append(5)
        for col in range(len(tmp)):
            if tmp[col]>5:
                warmhole[tmp[col]].append([row,col])
        mat.append(tmp)
    print(mat)
    print(warmhole)
    ans=0
    for i in range(1,N+1):
        for j in range(1,N+1):
            sx,sy=i,j
            if mat[i][j]:continue
            for k in range(4):
                cnt=0
                dn,dx,dy=ewsn[k]
                nx,ny=i+dx,j+dy
                while 1:
                    if [nx,ny]==[sx,sy] or mat[nx][ny]==-1:
                        if ans<cnt:ans=cnt
                        break
                    if 0<mat[nx][ny]<6:
                        dn,dx,dy=ewsn[direction[mat[nx][ny]][dn]]
                        cnt+=1
                    elif 5<mat[nx][ny]<11:
                        if [nx,ny]==warmhole[mat[nx][ny]][0]:
                            nx,ny=warmhole[mat[nx][ny]][1]
                        else:nx,ny=warmhole[mat[nx][ny]][0]
                    nx,ny=nx+dx,ny+dy
    print("#{} {}".format(tc+1,ans))
