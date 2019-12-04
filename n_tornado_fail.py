#n_tornado
n = int(input())

def fill_num():
    global A
    global flag_A
    global n
    cnt = 1
    i=0
    j=0
    d=0
    direction = [(1,0),(0,-1),(-1,0),(0,1)]
    while(cnt != n**2+1):
        A[i][j] = cnt
        flag_A[i][j] = True
        dic_x, dic_y = direction[d]
        i = i+dic_x
        j = j+dic_y
        cnt = cnt + 1
        
        if(d==3):
            if(i > n-1 or j > n-1 or i<0 or j<0 or flag_A[i][j]==True ):
                i = i - dic_x
                j = j - dic_y
                d=0
                dic_x, dic_y = direction[d]
                i = i + dic_x
                j = j + dic_y
        else:
            if(i > n-1 or j > n-1 or i<0 or j<0 or flag_A[i][j]==True):
                i = i - dic_x
                j = j - dic_y
                d=d+1
                dic_x, dic_y = direction[d]
                i = i + dic_x
                j = j + dic_y
        print(A)


A = list([0]*n for _ in range(n))
flag_A = list([False]*n for _ in range(n))


