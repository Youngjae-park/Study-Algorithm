T = int(input())

def func1(idx, cnt, visited, sum_):
    global min_
    global arr
    if sum_ > min_:
        return
    if idx <= cnt :
        min_ = min(min_, sum_)
        return
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            func1(idx, cnt+1, visited, sum_ + arr[cnt][i])
            visited[i] = False

for test_case in range(1,T+1):
    N = int(input())
    arr = [[]]*N
    visited = [False]*N
    min_ = 100000
    for i in range(N):
        arr[i] = list(map(int,input().split()))

    func1(N,0,visited, 0)
    print("#{} {}".format(test_case, min_))
