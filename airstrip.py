T = int(input())

def check(arr):
    temp = [0]*N
    for idx in range(len(arr)-1):
        '''
        if abs(arr[idx]-arr[idx+1]) == 0 and temp[idx+1] == -3:
            temp[idx] = 0
            temp[idx+1] = 0
        '''
        if abs(arr[idx]-arr[idx+1]) == 1:
            if arr[idx]>arr[idx+1]:
                #왼쪽이 1 더 클 때
                for i in range(1,X):
                    if i+idx > N-1:
                        return False
                    elif arr[i+idx] == arr[idx]-1:
                        temp[i + idx] = -1
                
                    
            else:
                #오른쪽이 1 더 클 때
                for i in range(-1, -X-1, -1):
                    if i+idx<0:
                        return False
                    elif arr[i+idx] == arr[idx]+1:
                        if temp[i+idx] == -1:
                            return False
                        else:
                            temp[i+idx] = 1
        elif not abs(arr[idx]-arr[idx+1]) == 0:
            return False
    print(temp)

    return True

for test_case in range(1, T+1):
    N, X = map(int, input().split())
    runway = [[] for _ in range(N)]
    check_height = [False]*N

    for i in range(N):
        runway[i] = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        runway_vertical = []
        runway_horizontal = runway[i][:]
        for j in range(N):
            runway_vertical.append(runway[j][i])
        print("runway_V", runway_vertical)
        print("runway_H", runway_horizontal)
        if check(runway_vertical):
            print("P_v")
            print("runway_V", runway_vertical)
            ans += 1
        if check(runway_horizontal):
            print("P_h")
            print("runway_H", runway_horizontal)
            ans += 1

    print("#{} {}".format(test_case, ans))
