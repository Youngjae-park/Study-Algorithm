#Palindrome
T = int(input())

def test():
    global arr
    global N
    global M
    global cnt
    global test_case
    
    stack = list()
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                if arr[i][j+k] == arr[i][j+M-1-k]:
                    cnt +=1
                    stack.append(arr[i][j+k])
                    if(cnt == M):
                        print("#{} {}".format(test_case, ''.join(stack)))
                        return
                else:
                    cnt = 0
                    stack.clear()

    stack.clear()
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                if arr[j+k][i] == arr[j+M-1-k][i]:
                    cnt += 1
                    stack.append(arr[j+k][i])
                    if(cnt == M):
                        print("#{} {}".format(test_case, ''.join(stack)))
                        return
                else:
                    cnt = 0
                    stack.clear()
    
        

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[]]*N
    cnt = 0
    for i in range(N):
        arr[i] = list(input())
    
    test()
