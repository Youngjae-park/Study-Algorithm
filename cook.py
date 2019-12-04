T = int(input())

def sol(n, arr, arr_A, arr_B, checked, idx_a, idx_b):
    global min_
    if n == N//2:
        #print(arr_A, arr_B)
        cnt_A = count(arr_A)
        cnt_B = count(arr_B)
        result = abs(cnt_A-cnt_B)
        if result<min_:
            min_ = result
        return
    else:
        for i in range(idx_a,N):
            if not checked[i]:
                checked[i] = True
                arr_A.append(i)
                for j in range(idx_b,N):
                    if not checked[j]:
                        checked[j] = True
                        arr_B.append(j)
                        sol(n+1, arr, arr_A, arr_B, checked, i+1, j+1)
                        checked[j] = False
                        arr_B.pop()
                checked[i] = False
                arr_A.pop()
                    



        '''
        for i in range(N):
            if not checked[i]:
                checked[i] = True
                arr_A.append(i)
                for j in range(N):
                    if not checked[j]:
                        checked[j] = True
                        arr_B.append(j)
                        sol(n+1, arr, arr_A, arr_B, checked)
                        arr_B.pop()
                        checked[j] = False
                arr_A.pop()
                checked[i] = False
        '''
        
def count(arr_X):
    sum_ = 0
    for a in arr_X:
        for b in arr_X:
            sum_ += arr_S[a][b]
    return sum_

        
    

for test_case in range(1, T+1):
    N = int(input())
    arr_S = [list(map(int, input().split())) for _ in range(N)]
    min_ = 99999
    check = [False] * N

    sol(0, arr_S, [], [], check, 0, 0)

    print("#{} {}".format(test_case, min_))
